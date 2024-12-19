fetch('http://localhost:8000/Velib/location.json')

    .then(response => response.json())
    .then(data => {
        if (data && Array.isArray(data)) {
            data.forEach(station => {
                L.marker([station.latitude, station.longitude])
                    .bindPopup(`<strong>${station.nom}</strong>`)
                    .addTo(map);
            });
        } else {
            console.error("Données incorrectes ou vides.");
        }
    })
    .catch(error => console.error('Erreur lors de la récupération des données :', error));



