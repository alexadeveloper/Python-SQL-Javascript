// replaces the name of this URL
$.get('https://swapi.co/api/people/5/?format=json', function (data, stat) {
  $('div#character').text(data.name);
});
