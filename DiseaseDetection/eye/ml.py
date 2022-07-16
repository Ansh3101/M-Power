import cv2
import torch
import torchvision
import cv2
import numpy as np
from torch import nn
import timm
import torch.nn.functional as F

def getModel():
    label2pred = {'Cataracts': 0, 'Glaucoma': 1, 'Healthy': 2, 'Uveitis': 3}
    n_classes = 4
    class IrisDisease(torch.utils.data.Dataset):
        def __init__(self, image_paths, labels, transforms=None):
            super(IrisDisease, self).__init__()
            self.image_paths = image_paths
            self.labels = labels
            self.transforms = transforms
        def __len__(self):
            return len(self.image_paths)
        def __getitem__(self, idx):
            image = cv2.imread(self.image_paths[idx])
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (224, 224))
            label = self.labels[idx]
            label = label2pred[label]
            label = torch.tensor(label)
            if self.transforms:
                image = self.transforms(image)
            return image, label        
    device='mps'
    tr_transforms = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.RandomHorizontalFlip(1.0),
        torchvision.transforms.CenterCrop(224),
        torchvision.transforms.RandomRotation(60),
        torchvision.transforms.RandomVerticalFlip(1.0),
        torchvision.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    val_transforms = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        torchvision.transforms.Resize((224,224))
    ])
    class ClassificationBase(nn.Module):
        def training_step(self, batch):
            images, labels = batch
            images = images.to(device)
            labels = labels.to(device)
            out = self(images)
            loss = F.cross_entropy(out, labels)
            acc = accuracy(out, labels)          
            return loss, acc
        def validation_step(self, batch):
            images, labels = batch 
            images = images.to(device)
            labels = labels.to(device)
            out = self(images)                    
            loss = F.cross_entropy(out, labels)  
            acc = accuracy(out, labels)          
            return {'val_loss': loss.detach(), 'val_acc': acc}
        def validation_epoch_end(self, outputs):
            batch_losses = [x['val_loss'] for x in outputs]
            epoch_loss = torch.stack(batch_losses).mean()   
            batch_accs = [x['val_acc'] for x in outputs]
            epoch_acc = torch.stack(batch_accs).mean()    
            return {'val_loss': epoch_loss.item(), 'val_acc': epoch_acc.item()}        
        def epoch_end(self, epoch, result):
            print("Epoch [{}], val_loss: {:.4f}, val_acc: {:.4f}".format(epoch, result['val_loss'], result['val_acc']))
    def accuracy(outputs, labels):
        _, preds = torch.max(outputs, dim=1)
        return torch.tensor(torch.sum(preds == labels).item() / len(preds))
    def evaluate(model, val_loader):
        outputs = [model.validation_step(batch) for batch in val_loader]
        return model.validation_epoch_end(outputs)
    class EfficientNetB0(ClassificationBase):
        def __init__(self):
            super().__init__()
            self.network = timm.create_model('efficientnet_b0', pretrained=True)
            num_ftrs = self.network.classifier.in_features
            self.network.classifier = nn.Linear(num_ftrs, n_classes)
        def forward(self, batch):
            batch = batch.to(device)
            return torch.sigmoid(self.network(batch))
    model = EfficientNetB0()
    model = model.to('mps')
    model.load_state_dict(torch.load('/Users/deveshkedia/Desktop/Projects/Doing/M-Power/DiseaseDetection/Models/model_trained.pth'))
    model.eval()
    return model
val_transforms = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        torchvision.transforms.Resize((224,224))
    ])
