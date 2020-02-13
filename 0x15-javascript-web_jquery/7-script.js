const url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, data => {
  $('DIV#character').text(data.name);
});
