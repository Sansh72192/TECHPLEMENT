document.addEventListener('DOMContentLoaded', () => {
    const quoteText = document.getElementById('quote-text');
    const quoteAuthor = document.getElementById('quote-author');
    const form = document.getElementById('quote-form');
    const authorInput = document.getElementById('author');

    function fetchQuote(author = "") {
        const url = `/get-quote/?author=${encodeURIComponent(author)}`;
        fetch(url)
            .then(res => res.json())
            .then(data => {
                quoteText.textContent = `"${data.quote}"`;
                quoteAuthor.textContent = `— ${data.author}`;
            });
    }

    // Load random quote on start
    fetchQuote();

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        fetchQuote(authorInput.value);
    });
});
