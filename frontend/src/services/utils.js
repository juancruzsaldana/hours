export const moneyFormater = new Intl.NumberFormat('es-AR', {style:'currency', currency: 'ARS'});
export const dollarFormater = new Intl.NumberFormat('en-US', {style:'currency', currency: 'USD'});
export const dynamicMoney = (lang, currencyCode) => {
    return new Intl.NumberFormat(lang, {style:'currency', currency: currencyCode});
}