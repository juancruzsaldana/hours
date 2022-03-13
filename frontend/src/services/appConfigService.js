const features = env?.FEATURES;
const home = env?.HOME;
const rate = env?.RATE;
class AppConfigService {
    getFeatures () {
        let items = []
        if(typeof features !== 'undefined' && features.length){
            items = features.split(', ');
            return {sidebarItems: items, home: home}
        }
        return {sidebarItems:items, home:'/'};
    }
    getRate(){
        return rate;
    }
}

const appConfigService = new AppConfigService();
export default appConfigService;