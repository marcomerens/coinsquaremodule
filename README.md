# Module: COINSQUARE crypto currency values

The 'COINSQUARE' module is a costum module for [MagicMirror](https://github.com/MichMich/MagicMirror). It displays the market values as they are available and published on [COINSQUARE](https://coinsquare.com/markets/bitcoin)

The module displays the currency you selected in the configuration file, its value in the base currency (USD or CAD) and the change of the value in teh last 24h.

The data comes from an unpublished API of COINSQUARE (you can see it in the python script which does the GET request).

The data is updated every minute.

## Installation instructions 
Just pull down this repo and copy it in the modules folder under your Magic Mirror installation folder


## Using the module

To use this module, add it to the modules array in the `config/config.js` file:
````javascript
modules: [
  {
    module: 'COINSQUARE',
    position: 'top_right',  // This can be any of the regions.
    config: {
      // See 'Configuration options' for more information.
      base:"USD",
      currencies:["ETH","BTC"]

    }
  }
]
````

## Configuration options

<table width="100%">
  <!-- why, markdown... -->
  <thead>
    <tr>
      <th>Option</th>
      <th width="100%">Description</th>
    </tr>
  <thead>
  <tbody>
    <tr>
      <td><code>base</code></td>
      <td>This is the currency you want the crypto currencies to be displayed in. Can be USD, CAD, EUR or GPB.
      </td>
    </tr>
    <tr>
      <td><code>currencies</code></td>
      <td>This is an array of the crypto currencies you want to display. Can be BTC, ETH, DOGE, BAB, LTC, DASH, XLM. The order of the array is the order the will be displayed.
      </td>
    </tr>
  </tbody>
</table>
