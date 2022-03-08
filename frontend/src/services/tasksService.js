
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
                        subtasks: [...(acc.subtasks || []), task]
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