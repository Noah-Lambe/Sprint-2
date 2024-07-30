fetch('./watches.json')
  .then(response => response.json())

  .then(data => {
    const watchListContainer = document.getElementById('watch-list');
    const sortedListContainer = document.getElementById('sorted-list');

    data.forEach(watch => {
      const watchInfo = document.createElement('div');
      watchInfo.innerHTML = `
        <p><strong>Full Name:</strong> ${getFullName(watch)}</p>
        <p><strong>Stock Status:</strong> ${checkStock(watch)}</p>
        <p><strong>Days Since Last Sold:</strong> ${daysSinceLastSold(watch)}</p>
        <hr>
      `;
      watchListContainer.appendChild(watchInfo);
    });

    const sortedData = sortByPrice(data);
    sortedListContainer.innerHTML = '<h2>Our Selection Sorted by Price</h2>';
    sortedData.forEach(watch => {
      const sortedWatchInfo = document.createElement('div');
      sortedWatchInfo.innerHTML = `
        <ul>
        <li><p>${watch.brand} ${watch.name}</p></li>
        <p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspPrice: <strong>${watch.price}</strong></p>
        
        </ul>
      `;
      sortedListContainer.appendChild(sortedWatchInfo);
    });

    data.forEach(watch => {
    console.log(getFullName(watch));
    console.log(checkStock(watch));
    console.log(daysSinceLastSold(watch));
    });

    console.log(sortByPrice(data));
  })
  .catch(error => {
    console.error(error);
  });

  function getFullName(watch) {
    return `${watch.brand} ${watch.name}`;
  }
  function daysSinceLastSold(watch) {
    const today = new Date();
    const lastSoldDate = new Date(watch["last sold"]);
    const timeDiff = today - lastSoldDate;
    const daysDiff = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
    return `${daysDiff} days since last sale`;
  }
  function checkStock(watch) {
    if (watch["on hand"] > 0) {
        return `The ${watch.name} is in stock`;
      } else {
        return `The ${watch.name} is out of stock`;
      }
}
  function sortByPrice(watches, ascending = true) {
    return watches.slice()
        .sort((a, b) => {
        const priceA = parseFloat(a.price.replace(/[$,]/g, ''));
        const priceB = parseFloat(b.price.replace(/[$,]/g, ''));
        return ascending ? priceA - priceB : priceB - priceA;
    })
    .map(watch => ({
        brand: watch.brand,
        name: watch.name,
        price: watch.price,
    }));
}

