const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://stock-analysis.p.rapidapi.com/api/v1/resources/earnings-estimate',
  params: {ticker: 'AAPL'},
  headers: {
    'X-RapidAPI-Key': 'd3234f9b98msh636f82f9af5f491p15d26ejsn2b89beb2bdc9',
    'X-RapidAPI-Host': 'stock-analysis.p.rapidapi.com'
  }
};

try {
	const response = await axios.request(options);
	console.log(response.data);
} catch (error) {
	console.error(error);
}