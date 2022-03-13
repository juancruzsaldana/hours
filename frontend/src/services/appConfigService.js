const features = env?.FEATURES;

class AppConfigService {
    getFeatures () {
        if(typeof features !== 'undefined' && features.length){
            return features.split(', ');
        }
        return [];
    }
}

const appConfigService = new AppConfigService();
export default appConfigService;