document.addEventListener('DOMContentLoaded', function() {
  const quotes = [
    "Strive not to be a sucess, but rather to be of value – Albert Einstein",
    "I have not failed. I've just found 10,000 ways that won't work - Thomas Edison",
    "Be stubborn on vision, but flexible on details - Jeff Bezoz"

    // ... add as many quotes as you like
  ];

  function displayRandomQuote() {
    const quoteElement = document.getElementById('random-quote');
    if (quoteElement) { // Check if the element actually exists
      const randomIndex = Math.floor(Math.random() * quotes.length);
      quoteElement.textContent = quotes[randomIndex];
    } else {
      console.error('Element with ID "random-quote" was not found.');
    }
  }

  displayRandomQuote();
});
