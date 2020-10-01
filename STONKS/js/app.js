// Create a page which allows users to search for stock quotes. The page will consist of a TextBox where users can enter the symbol of the stock they are looking for. 
// When the presses the "Show Quotes" button the app will call the "getStockQuote" function implemented in stockQuotes.js (attached) and get the stock quotes. 
// You should update the quotes every 2 seconds by making a call to getStockQuote function. Your app should display the name of the stock and also the price of the stock.

let textBox = document.getElementById("textBox");
let submitButton = document.getElementById("submitButton");
let displayEl = document.getElementById("displayEl");

submitButton.addEventListener("click", () => {
    let symbol = textBox.value;
    let value = getStockQuote(symbol);
    let name = value.name;
    let price = value.price;

    displayEl.innerHTML = `${name}: $${price}`;
    
    window.setInterval(() => {
    let symbol = textBox.value;
    let value = getStockQuote(symbol);
    let name = value.name;
    let price = value.price;

    displayEl.innerHTML = `${name}: $${price}`;}, 2000);
});

