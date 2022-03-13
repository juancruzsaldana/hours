const features = env?.FEATURES;
const home = env?.HOME;
class AppConfigService {
    getFeatures () {
        let items = []
        if(typeof features !== 'undefined' && features.length){
            items = features.split(', ');
            return {sidebarItems: items, home: home}
        }
        return {sidebarItems:items, home:'/'};
    }
}

const appConfigService = new AppConfigService();
export default appConfigService;