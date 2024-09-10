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
        `<li onclick="selectSuggestion('${symbol}'); fetchStockData('${symbol}')">${symbol}</li>`
    ).join('');
}

function selectSuggestion(symbol) {
    document.getElementById('search').value = symbol;
    document.getElementById('suggestions').innerHTML = '';
}


// Função para buscar os dados da ação e renderizar o gráfico.
function fetchStockData(ticker) {
    fetch(`/dashboard/get-stock-data/?ticker=${ticker}`)
        .then(response => response.json())
        .then(data => {
            if (data.graph) {
                var graphData = JSON.parse(data.graph);
                Plotly.newPlot('graph-container', graphData.data, graphData.layout);
            } else {
                console.error('Erro ao buscar dados da ação:', data.error);
            }
        })
        .catch(error => console.error('Erro:', error));
}

// Função para renderizar o gráfico
function loadGraph() {
    const graphData = JSON.parse('{{ graph|safe }}');
    if (graphData) {
        Plotly.newPlot('graph-container', graphData.data, graphData.layout);
    } else {
        fetch('/fetch-token-data/')
            .then(response => response.json())
            .then(data => {
                if (data.graph) {
                    Plotly.newPlot('graph-container', JSON.parse(data.graph).data, JSON.parse(data.graph).layout);
                } else {
                    console.error('Erro ao buscar dados da ação:', data.error);
                }
            });
    }
}
