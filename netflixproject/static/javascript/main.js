const url = 'https://imdb8.p.rapidapi.com/auto-complete?q=game';
const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '6aba722c6bmshbe4e6e1e623e9c4p1b92e4jsn242f87b53d63',
		'X-RapidAPI-Host': 'imdb8.p.rapidapi.com'
	}
};

try {
	const response = await fetch(url, options);
	const result =await response.json();
	console.log(result);
} catch (error) {
	console.error(error);
}
