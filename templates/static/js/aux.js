function makeEditable(fieldId) {
    const inputField = document.getElementById(fieldId);
    inputField.removeAttribute('readonly');
    inputField.focus();

    inputField.addEventListener('blur', function() {
        inputField.setAttribute('readonly', true);
        const fieldValue = inputField.value;

        // Envia a atualização via AJAX
        fetch('/update-profile-field/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Para incluir o CSRF token
            },
            body: JSON.stringify({
                field: fieldId,
                value: fieldValue
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                console.log(`${fieldId} updated successfully`);
            } else {
                console.error(`Failed to update ${fieldId}`);
            }
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
            // Verifica se o cookie começa com o nome dado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function toggleEdit(field) {
    var input = document.getElementById(field);
    var icon = document.getElementById(field + '-icon');

    if (input.readOnly) {
        input.readOnly = false;
        icon.textContent = '✔';  // Troca para ícone de "certo"
    } else {
        // Enviar os dados para o servidor via AJAX
        saveChanges(field, input.value);
        
        input.readOnly = true;
        icon.textContent = '✎';  // Volta para a caneta
    }
}

function saveChanges(field, value) {
    // Exemplo de envio de dados via AJAX
    fetch(`/auth/update-${field}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        body: JSON.stringify({ value: value })
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            alert('Failed to update ' + field);
        }
    });
}

// Event LIstener para adicionar gráfico na página
document.addEventListener('DOMContentLoaded', function() {
    fetch('/dashboard/get-graph/')
        .then(response => response.json())
        .then(data => {
            const graphElement = document.getElementById('graph-container');
            if (data.graph) {
                Plotly.react(graphElement, JSON.parse(data.graph), {});
            }
        });
});




function toggleMonitoringPeriodEdit() {
    var select = document.getElementById('monitoringPeriod');
    var icon = document.getElementById('monitoringPeriod-icon');

    if (select.disabled) {
        select.disabled = false;
        icon.textContent = '✔';  // Troca para ícone de "certo"
    } else {
        // Enviar os dados para o servidor via fetch
        saveMonitoringPeriodChanges(select.value);
        
        select.disabled = true;
        icon.textContent = '✎';  // Volta para a caneta
    }
}

function saveMonitoringPeriodChanges(value) {
    fetch('/auth/update-monitoring-period/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Inclua o token CSRF se estiver usando Django
        },
        body: JSON.stringify({
            field: 'monitoringPeriod',
            value: value
        })
    })
    .then(response => {
        if (response.ok) {
            console.log('Alteração salva com sucesso.');
        } else {
            console.error('Erro ao salvar alteração.');
        }
    })
    .catch(error => {
        console.error('Erro na requisição:', error);
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
