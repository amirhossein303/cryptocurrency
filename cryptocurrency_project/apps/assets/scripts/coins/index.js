const websocket_url = 'ws://' + window.location.host + '/ws/coins/'
const coinsWebsocket = new WebSocket(websocket_url)

coinsWebsocket.onopen = function(e) {
    console.info('Websocket connected.')
}

coinsWebsocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    data.forEach(element => {
        update_coin(element)
    });
};

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function update_coin(coin) {
    let table_row = document.getElementById(coin.symbol);
    let table_data = table_row.getElementsByTagName('td');
    let coin_price = table_data[2];
    let market_cap = table_data[3];
    let percent_change_24h = table_data[4];
    let percent_change_7d = table_data[5];
    let divs_for_percent_chnage_24h = percent_change_24h.getElementsByTagName('div')
    divs_for_percent_chnage_24h[0].classList.add('pulse-animation');
    setTimeout(() => {
        divs_for_percent_chnage_24h[0].classList.remove('pulse-animation');
    }, 500);
    
    if (coin.quote.USD.percent_change_24h >= 0) {
        divs_for_percent_chnage_24h[0].classList.remove('badge-danger');
        divs_for_percent_chnage_24h[0].classList.add('badge-success');
    } else {
        divs_for_percent_chnage_24h[0].classList.remove('badge-success');
        divs_for_percent_chnage_24h[0].classList.add('badge-danger');
    }
    
    coin_price.textContent = '$' + numberWithCommas(coin.quote.USD.price.toFixed(1));
    market_cap.textContent = numberWithCommas(coin.quote.USD.market_cap.toFixed(1));
    divs_for_percent_chnage_24h[1].textContent = numberWithCommas(coin.quote.USD.percent_change_24h.toFixed(2)) + '%';
    percent_change_7d.textContent = numberWithCommas(coin.quote.USD.percent_change_7d.toFixed(2)) + '%';

}