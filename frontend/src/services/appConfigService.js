const features = env?.FEATURES;
const home = env?.HOME;
const rate = env?.RATE;;
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
export const base_url = env?.API_URL;
export const media_url = env?.MEDIA_URL;