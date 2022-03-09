
import moment from "moment";
import 'moment-duration-format';
const base_url = env?.API_URL;
const rate = env?.RATE;
const document = env?.GOOGLESHEET;


class TasksService {
    getTasks(start_date = '2022-01-01T15:00:00-03:00', end_date = '2022-01-31T16:00:00-03:00') {
        return new Promise(async (resolve, reject) => {
            const endpoint = `${base_url}tasks?start_date=${start_date}&end_date=${end_date}`;
            let response = await fetch(endpoint);
            let tasks = await response.json();
            //let tasks = [{"pid":10,"tasks":[{"id":2392310528,"guid":"74fadc27b11915d9019e29d7ee167676","wid":4237446,"billable":false,"start":"2022-03-02T14:45:36+00:00","stop":"2022-03-02T14:46:40+00:00","duration":"64","description":"coco","duronly":false,"at":"2022-03-02T14:47:35+00:00","uid":5686429,"pid":0}],"project":{"data":{"name":"Agencia","id":10,"hex_color":"#dddddd"}}},{"pid":175206937,"tasks":[{"id":2390485859,"guid":"b77b015414dd82adaa8b641088ca575b","wid":4237446,"billable":false,"start":"2022-03-01T15:16:45+00:00","stop":"2022-03-01T15:29:56+00:00","duration":"791","description":"Bug filter dt","duronly":false,"at":"2022-03-01T15:29:58+00:00","uid":5686429,"pid":175206937},{"id":2390558995,"guid":"04b3c35476437f3f7ed92ee403d7afe3","wid":4237446,"billable":false,"start":"2022-03-01T15:52:03+00:00","stop":"2022-03-01T15:56:12+00:00","duration":"249","description":"deploy bugfix","duronly":false,"at":"2022-03-01T15:56:13+00:00","uid":5686429,"pid":175206937},{"id":2390576746,"guid":"cef91c42891c1d40052d9bd13826e81b","wid":4237446,"billable":false,"start":"2022-03-01T16:00:14+00:00","stop":"2022-03-01T16:11:39+00:00","duration":"685","description":"deploy bugfix","duronly":false,"at":"2022-03-01T16:11:40+00:00","uid":5686429,"pid":175206937},{"id":2392883639,"guid":"cb491d7014394b4f4e8b14fe3af9cc2b","wid":4237446,"billable":false,"start":"2022-03-02T20:14:34+00:00","stop":"2022-03-02T20:33:11+00:00","duration":"1117","description":"demo con john","duronly":false,"at":"2022-03-02T20:33:12+00:00","uid":5686429,"pid":175206937},{"id":2393885996,"guid":"e3dcdfcd4d83ce1bd0e4126729e8432f","wid":4237446,"billable":false,"start":"2022-03-03T12:07:04+00:00","stop":"2022-03-03T14:15:18+00:00","duration":"7694","description":"bug fix","duronly":false,"at":"2022-03-03T14:15:20+00:00","uid":5686429,"pid":175206937},{"id":2394404070,"guid":"7bc0c5683525b27f2e08d5036d2e864f","wid":4237446,"billable":false,"start":"2022-03-03T16:39:31+00:00","stop":"2022-03-03T17:39:58+00:00","duration":"3627","description":"bug fix","duronly":false,"at":"2022-03-03T17:40:00+00:00","uid":5686429,"pid":175206937},{"id":2400124479,"guid":"cecc0009073ac4e85816f650207e9860","wid":4237446,"billable":false,"start":"2022-03-08T13:04:16+00:00","stop":"2022-03-08T13:21:31+00:00","duration":"1035","description":"Diagnóstico listado de gastos","duronly":false,"at":"2022-03-08T13:21:33+00:00","uid":5686429,"pid":175206937},{"id":2400219826,"guid":"19eaeae0c2a60886510663250350ebb1","wid":4237446,"billable":false,"start":"2022-03-08T13:56:28+00:00","stop":"2022-03-08T14:14:10+00:00","duration":"1062","description":"Diagnóstico listado de gastos","duronly":false,"at":"2022-03-08T14:14:12+00:00","uid":5686429,"pid":175206937},{"id":2400264176,"guid":"f80bbe49fd50e599702332cfa32d1a90","wid":4237446,"billable":false,"start":"2022-03-08T14:16:53+00:00","stop":"2022-03-08T15:27:16+00:00","duration":"4223","description":"entorno de desarrollo","duronly":false,"at":"2022-03-08T15:27:19+00:00","uid":5686429,"pid":175206937}],"project":{"data":{"id":175206937,"wid":4237446,"name":"fullmotos","billable":false,"is_private":true,"active":true,"template":false,"at":"2021-10-04T19:27:59+00:00","created_at":"2021-10-04T19:27:59+00:00","color":"10","auto_estimates":false,"actual_hours":129,"hex_color":"#c7af14"}}},{"pid":174206699,"tasks":[{"id":2392231997,"guid":"f4a1a4d7d8b59f0fca21f90d60499688","wid":4237446,"billable":false,"start":"2022-03-02T14:08:41+00:00","stop":"2022-03-02T14:45:30+00:00","duration":"2209","description":"documentos interface","duronly":false,"at":"2022-03-02T14:45:34+00:00","uid":5686429,"pid":174206699},{"id":2392314583,"guid":"7713cab888f258832bb81fec821824b6","wid":4237446,"billable":false,"start":"2022-03-02T14:47:37+00:00","stop":"2022-03-02T20:14:13+00:00","duration":"19596","description":"documentos interface","duronly":false,"at":"2022-03-02T20:14:15+00:00","uid":5686429,"pid":174206699},{"id":2392908713,"guid":"4297706bd0e1434e5202044198442b71","wid":4237446,"billable":false,"start":"2022-03-02T20:33:11+00:00","stop":"2022-03-02T20:58:23+00:00","duration":"1512","description":"documentos interface","duronly":false,"at":"2022-03-02T20:58:24+00:00","uid":5686429,"pid":174206699},{"id":2398947570,"guid":"fe381b8be9c1147c85b0f3681a1734ce","wid":4237446,"billable":false,"start":"2022-03-07T19:01:37+00:00","stop":"2022-03-07T19:19:39+00:00","duration":"1082","description":"Demo","duronly":false,"at":"2022-03-07T19:19:54+00:00","uid":5686429,"pid":174206699}],"project":{"data":{"id":174206699,"wid":4237446,"name":"ministerio","billable":false,"is_private":true,"active":true,"template":false,"at":"2021-09-07T18:26:48+00:00","created_at":"2021-09-07T18:26:48+00:00","color":"6","auto_estimates":false,"actual_hours":275,"hex_color":"#06a893"}}},{"pid":160327043,"tasks":[{"id":2396320858,"guid":"e2f76eb94d77e8285a687995a1a5e53a","wid":4237446,"billable":false,"start":"2022-03-04T19:16:21+00:00","stop":"2022-03-04T20:56:44+00:00","duration":"6023","description":"Actualización apps mobiles","duronly":false,"at":"2022-03-04T21:31:30+00:00","uid":5686429,"pid":160327043}],"project":{"data":{"id":160327043,"wid":4237446,"name":"Ventas en red","billable":false,"is_private":true,"active":true,"template":false,"at":"2020-06-09T04:17:48+00:00","created_at":"2020-05-01T15:30:51+00:00","color":"11","auto_estimates":false,"actual_hours":101,"hex_color":"#566614"}}}]
            
            let formatedTasks = this.formatTasks(tasks);
            resolve(formatedTasks)
        });
    }
    formatTasks (tasksStructure){
        let totalStructure ={
            tasks: [],
            pid: 0,
            project: {
                data:{
                    id: 0,
                    name: 'Totales',
                    hex_color: "#1e3a8a",
                }
            }
        };
        let totalHours = 0;
        let mapedTasks = tasksStructure.map((structure) => {
            let {tasks, project, pid} = structure;
            let key = '';
            const groupedByDescription = tasks.reduce((acc, task) => {
                key = `${task.description}${moment(task.start).format('DDMMYYYY')}`;
                return {
                    ...acc,
                    [key]: [ ...(acc[key] || []), task]
                }
            }, {});
            let projectDuration = 0;
            let reducedTasks = [];
            let taskItem = [];
            for(let description in groupedByDescription){
                taskItem = groupedByDescription[description].reduce((acc, task) => {
                    return {
                        at: acc.at || task.at,
                        billable: task.billable,
                        count: acc.count? acc.count + 1: 1,
                        description: task.description,
                        duration: acc.duration? Number(acc.duration) + Number(task.duration) : Number(task.duration),
                        duronly: task.duronly,
                        end: task.end || acc.end,
                        guid: acc.guid? `${acc.guid}, ${task.guid}` : task.guid,
                        id: acc.id? `${acc.id}, ${task.id}`: task.id,
                        pid: task.pid,
                        start: acc.start || task.start,
                        stop: task.stop,
                        uid: task.uid,
                        wid: task.wid,
                        subtasks: [...(acc.subtasks || []), {...task, duration: moment.utc(task.duration * 1000).format('H:mm:ss')}]
                    }
                }, {});
                reducedTasks.push(taskItem);
                projectDuration += taskItem.duration;
            }
            
            let procesedTask = reducedTasks.map((task) => {
                task.duration = moment.utc(task.duration * 1000).format('H:mm:ss');
                task.date = moment(task.start).format('DD-MM-YYYY');
                task.start = moment(task.start).format('HH:mm:ss');
                task.end = moment(task.end).format('DD-MM-YYYY');
                task.stop = moment(task.stop).format('HH:mm:ss');
                return task;
            })
            totalHours += projectDuration;
            totalStructure.tasks.push({
                duration: moment.duration(projectDuration, 'seconds').format('H:mm:ss',{trim: false}),
                date: moment(project.data.created_at).format('DD-MM-YYYY'),
                start: '',
                end: '',
                stop: '',
                description: project.data.name,
            }); 
            return {
                project: {...project, durationFormated: moment.duration(projectDuration, 'seconds').format('H:mm:ss',{trim: false}), durationHours:  projectDuration /( 60 * 60)},
                tasks: procesedTask,
                pid, pid
            }
        });
        totalStructure.project.durationFormated = moment.duration(totalHours, 'seconds').format('H:mm:ss',{trim: false});
        totalStructure.project.durationHours = totalHours /( 60 * 60);
        return [totalStructure, ...mapedTasks];
    }
    getRate(){
        return rate;
    }

    writeInGdoc (data) {
        data = this.getRequestStructure(data);
        return new Promise(async (resolve, reject) => {
            const endpoint = `${base_url}updatesheet/`;
            let response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify( data)
            });
            let r = await response.json();
            resolve({result: r})
        });
    }

    getRequestStructure(data){
        let structureArray = data.map((sheet )=> {
            return {
                [sheet.project.data.name] : {
                    tasks: sheet.tasks.map((t) => ({
                        description: t['description'], 
                        ...(sheet.pid !== 0? {date: t['date']} : {}),  
                        ...(sheet.pid !== 0? {duration: t['duration']} : {})
                    }))
                }
            }
        });
        let structureObject = {};
        structureArray.forEach((sheet) => {
            structureObject = {
                ...structureObject,
                ...sheet
            }
        });
        return {
            document: document,
            structure: structureObject,
            rate: rate
        }
    }
}

const tasksService = new TasksService();
export default tasksService;