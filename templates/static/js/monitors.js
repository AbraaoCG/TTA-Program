// Função para criar Monitor
function submitMonitor() {
    const upper = document.getElementById('upper').value;
    const bottom = document.getElementById('bottom').value;

    // Enviar o pedido POST via fetch
    fetch('/dashboard/set-monitor/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // Pega o CSRF token
        },
        body: JSON.stringify({
            upper: upper,
            bottom: bottom
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // alert("Monitor set successfully!");
            reloadStockMonitors();  // Recarrega a lista de StockMonitors
        } else {
            alert(data.error);
        }
    });
}

// Função para recarregar a lista de StockMonitors
function reloadStockMonitors() {
    fetch('/dashboard/get-stock-monitors/')
        .then(response => response.json())
        .then(data => {
            const container = document.querySelector('.stock-monitor-container');
            container.innerHTML = '';  // Limpa a lista atual

            // Recria os blocos com os novos dados
            data.stock_monitors.forEach(monitor => {
                const monitorBlock = document.createElement('div');
                monitorBlock.classList.add('stock-monitor-block');
                
                monitorBlock.innerHTML = `
                    <h3>${monitor.symbol}</h3>
                    <div class="monitor-info">
                        <div class="info-left">
                            <div>
                                <label for="upper-${monitor.symbol}">Upper:</label>
                                <input type="text" id="upper-${monitor.symbol}" value="${monitor.supLimit}" readonly>
                            </div>
                            <div>
                                <label for="bottom-${monitor.symbol}">Bottom:</label>
                                <input type="text" id="bottom-${monitor.symbol}" value="${monitor.botLimit}" readonly>
                            </div>
                        </div>
                        <div class="info-right">
                            <span id="${monitor.symbol}-icon" class="edit-icon" onclick="toggleEditMonitor('${monitor.symbol}')">✎</span>
                            <span class="delete-icon" onclick="deleteMonitor('${monitor.symbol}')">🗑️</span>
                        </div>
                    </div>
                `;
                container.appendChild(monitorBlock);
            });
        });
}


// Função para obter o CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function toggleEditMonitor(symbol) {
    const upperInput = document.getElementById(`upper-${symbol}`);
    const bottomInput = document.getElementById(`bottom-${symbol}`);
    const editIcon = document.getElementById(`${symbol}-icon`);

    if (editIcon.textContent === '✎') {
        // Mudar o ícone para confirmação e tornar os campos editáveis
        editIcon.textContent = '✔';
        upperInput.removeAttribute('readonly');
        bottomInput.removeAttribute('readonly');
    } else {
        // Mudar o ícone de volta para edição e salvar as alterações
        editIcon.textContent = '✎';
        upperInput.setAttribute('readonly', true);
        bottomInput.setAttribute('readonly', true);
        saveMonitorChanges(symbol);
    }
}

function saveMonitorChanges(symbol) {
    const upperLimit = document.querySelector(`#${symbol}-upper`).value;
    const bottomLimit = document.querySelector(`#${symbol}-bottom`).value;

    fetch(`/dashboard/save-monitor-changes/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: JSON.stringify({ symbol: symbol, upper: upperLimit, bottom: bottomLimit })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Atualizar a lista de monitores ou exibir uma mensagem de sucesso
            location.reload(); // Recarregar a página para atualizar a lista
        } else {
            alert('Failed to save changes');
        }
    });
}


function deleteMonitor(symbol) {
    fetch('/dashboard/delete-monitor/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Pega o CSRF token
        },
        body: JSON.stringify({ symbol: symbol })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Recarregar apenas a lista de monitores
            reloadStockMonitors();
        } else {
            alert('Failed to delete monitor');
        }
    });
}
