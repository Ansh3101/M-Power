
let loader = document.getElementById('loader');
let content = document.getElementById("content")
let form = document.getElementById("form")
form.addEventListener('submit', function (e) {
  e.preventDefault();
  content.classList.add("hidden")
  loader.classList.remove('hidden');
  form.submit();
});