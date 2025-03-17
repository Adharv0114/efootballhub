function searchPlayers() {
    let query = document.getElementById("searchInput").value;
    fetch(`/api/players/search/?q=${query}`)
        .then(response => response.json())
        .then(data => {
            let resultsDiv = document.getElementById("playerResults");
            resultsDiv.innerHTML = "";
            data.forEach(player => {
                resultsDiv.innerHTML += `<p>${player.name} - ${player.position} (${player.overall_rating})</p>`;
            });
        })
        .catch(error => console.error('Error:', error));
}

function comparePlayers() {
    let player1 = document.getElementById("player1").value;
    let player2 = document.getElementById("player2").value;

    fetch(`/api/players/compare/?player1=${player1}&player2=${player2}`)
        .then(response => response.json())
        .then(data => {
            let resultsDiv = document.getElementById("comparisonResults");
            resultsDiv.innerHTML = `
                <h2>Comparison</h2>
                <p><strong>${data.player1.name} vs ${data.player2.name}</strong></p>
                <p>Overall Rating: ${data.player1.overall_rating} - ${data.player2.overall_rating}</p>
                <p>Speed: ${data.player1.speed} - ${data.player2.speed}</p>
                <p>Passing: ${data.player1.passing} - ${data.player2.passing}</p>
            `;
        })
        .catch(error => console.error('Error:', error));
}

function createSquad() {
    let squadName = document.getElementById("squadName").value;
    let playerIds = document.getElementById("playerIds").value.split(',').map(id => parseInt(id.trim()));

    fetch("/api/squads/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: squadName,
            players: playerIds
        })
    })
    .then(response => response.json())
    .then(data => {
        let resultsDiv = document.getElementById("squadResults");
        resultsDiv.innerHTML = `<p>Squad Created: ${data.name}</p>`;
    })
    .catch(error => console.error('Error:', error));
}
