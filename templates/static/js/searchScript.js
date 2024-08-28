async function fetchSuggestions() {
    const query = document.getElementById('search').value;
    if (query.length === 0) {
        document.getElementById('suggestions').innerHTML = '';
        return;
    }

    const response = await fetch(`api/suggestions/?query=${query}`);
    const suggestions = await response.json();

    const suggestionsList = document.getElementById('suggestions');
    suggestionsList.innerHTML = suggestions.map(symbol => 
        `<li onclick="selectSuggestion('${symbol}')">${symbol}</li>`
    ).join('');
}

function selectSuggestion(symbol) {
    document.getElementById('search').value = symbol;
    document.getElementById('suggestions').innerHTML = '';
}
