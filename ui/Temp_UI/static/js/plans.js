// // displays a plan for given robot data
// function displayPlan() {
//     // clear the plan panel
//     let plans = document.getElementById("plans")
//     plans.innerHTML = ""

//     // if a robot is selected, fill in the robot info and plan
//     if (robotFilterId != -1) {
//         // robot class
//         let robotClass = document.createElement('div')
//         robotClass.classList.add("plan-info-tag")
//         robotClass.style.backgroundColor = "lightgrey"
//         robotClass.innerHTML = "Ground Vehicle"
//         plans.append(robotClass)

//         // last sync
//         let robotLastSync = document.createElement('div')
//         robotLastSync.classList.add("plan-info-tag")
//         robotLastSync.style.backgroundColor = "palelightblue"
//         robotLastSync.innerHTML = "Last Sync: " + Math.round(Date.now() / 1000 - savedRobotData[robotFilterId].lastSeen) + "s"
//         plans.append(robotLastSync)

//         let space = document.createElement("div")
//         space.style.height = "1.0rem";
//         plans.append(space);

//         // completed plan
//         let completedPlanTitle = document.createElement("div")
//         completedPlanTitle.innerHTML = "—— Completed Plan ——"
//         completedPlanTitle.classList.add("plan-info-title")
//         plans.append(completedPlanTitle)

//         if (savedRobotData[robotFilterId]) {
//             currentPlan = savedRobotData[robotFilterId].completedPlan
//             currentPlan.forEach((description) => {
//                 let task = document.createElement("div")
//                 task.classList.add("plan-info-tag")
//                 task.style.backgroundColor = colorCompletedPlan
//                 task.innerHTML = description
//                 plans.append(task)
//             });
//         }

//         // current plan
//         let currentPlanTitle = document.createElement("div")
//         currentPlanTitle.innerHTML = "—— Current Plan ——"
//         currentPlanTitle.classList.add("plan-info-title")
//         plans.append(currentPlanTitle)

//         if (savedRobotData[robotFilterId]) {
//             currentPlan = savedRobotData[robotFilterId]["currentAbstractedPlan"]
//             currentPlan.forEach((description) => {
//                 let task = document.createElement("div")
//                 task.classList.add("plan-info-tag")
//                 task.style.backgroundColor = colorCurrentPlan
//                 task.innerHTML = description
//                 plans.append(task)
//             });
//         }

//         space = document.createElement("div")
//         space.style.height = "1.0rem";
//         plans.append(space);

//         // previous plan
//         let previousPlanTitle = document.createElement("div")
//         previousPlanTitle.innerHTML = "—— Previous Plan ——"
//         previousPlanTitle.classList.add("plan-info-title")
//         plans.append(previousPlanTitle)

//         let previousPlan = ["Go to objective C", "Acquire package #1", "Go to base"]
//         previousPlan.forEach((description) => {
//             let task = document.createElement("div")
//             task.classList.add("plan-info-tag")
//             task.style.backgroundColor = colorPreviousPlan
//             task.innerHTML = description
//             plans.append(task)
//         });
//     }
// }


// displays a plan for given robot data
function displayPlan() {
    // clear the plan panel
    let plans = document.getElementById("plans")
    plans.innerHTML = ""

    // if a robot is selected, fill in the robot info and plan
    if (robotFilterId != -1) {
        // robot class
        let robotClass = document.createElement('div')
        robotClass.classList.add("plan-info-tag")
        robotClass.style.backgroundColor = "lightgrey"
        robotClass.innerHTML = "Quadruped robot "
        plans.append(robotClass)

        // last sync
        let robotLastSync = document.createElement('div')
        robotLastSync.classList.add("plan-info-tag")
        robotLastSync.style.backgroundColor = "palelightblue"
        robotLastSync.innerHTML = "Last Sync: " + Math.round(Date.now() / 1000 - savedRobotData[robotFilterId].lastSeen) + "s"
        plans.append(robotLastSync)

        let space = document.createElement("div")
        space.style.height = "1.0rem";
        plans.append(space);

        // completed plan
        /**
        let completedPlanTitle = document.createElement("div")
        completedPlanTitle.innerHTML = "—— Completed Plan ——"
        completedPlanTitle.classList.add("plan-info-title")
        plans.append(completedPlanTitle)

        if (savedRobotData[robotFilterId]) {
            let currentPlan = savedRobotData[robotFilterId].completedPlan || []
            currentPlan.forEach((description) => {
                let task = document.createElement("div")
                task.classList.add("plan-info-tag")
                task.style.backgroundColor = colorCompletedPlan
                task.innerHTML = description
                plans.append(task)
            });
        }
         */

        // current plan
        let currentPlanTitle = document.createElement("div")
        currentPlanTitle.innerHTML = "—— Current Plan ——"
        currentPlanTitle.classList.add("plan-info-title")
        plans.append(currentPlanTitle)

        if (savedRobotData[robotFilterId]) {
            let currentPlan = savedRobotData[robotFilterId]["currentAbstractedPlan"] || []
            currentPlan.forEach((description) => {
                let task = document.createElement("div")
                task.classList.add("plan-info-tag")
                task.style.backgroundColor = colorCurrentPlan
                task.innerHTML = description
                plans.append(task)
            });
        }

        space = document.createElement("div")
        space.style.height = "1.0rem";
        plans.append(space);

        // previous plan
        let previousPlanTitle = document.createElement("div")
        previousPlanTitle.innerHTML = "—— Previous Plan ——"
        previousPlanTitle.classList.add("plan-info-title")
        plans.append(previousPlanTitle)

        // Use actual previousAbstractedPlan instead of hardcoded values
        if (savedRobotData[robotFilterId]) {
            let previousPlan = savedRobotData[robotFilterId]["previousAbstractedPlan"] || []
            previousPlan.forEach((description) => {
                let task = document.createElement("div")
                task.classList.add("plan-info-tag")
                task.style.backgroundColor = colorPreviousPlan
                task.innerHTML = description
                plans.append(task)
            });
        }
    }
}