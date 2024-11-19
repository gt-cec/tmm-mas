// displays a plan for given robot data
function displayPlan(robot) {
    // clear the plan panel
    let plans = document.getElementById("plans")
    plans.innerHTML = ""

    // robot class
    let robotClass = document.createElement('div')
    robotClass.classList.add("plan-info-tag")
    robotClass.style.backgroundColor = "lightgrey"
    robotClass.innerHTML = "Ground Vehicle"
    plans.append(robotClass)

    // last sync
    let robotLastSync = document.createElement('div')
    robotLastSync.classList.add("plan-info-tag")
    robotLastSync.style.backgroundColor = "palelightblue"
    robotLastSync.innerHTML = "Last Sync: 48s"
    plans.append(robotLastSync)

    let space = document.createElement("div")
    space.style.height = "1.0rem";
    plans.append(space);

    // current plan
    let currentPlanTitle = document.createElement("div")
    currentPlanTitle.innerHTML = "—— Current Plan ——"
    currentPlanTitle.classList.add("plan-info-title")
    plans.append(currentPlanTitle)

    let currentPlan = ["Go to objective A", "Acquire package #3", "Go to objective C", "Drop package #3", "Go to base"]
    currentPlan.forEach((description) => {
        let task = document.createElement("div")
        task.classList.add("plan-info-tag")
        task.style.backgroundColor = "palegreen"
        task.innerHTML = description
        plans.append(task)
    });

    space = document.createElement("div")
    space.style.height = "1.0rem";
    plans.append(space);

    // previous plan
    let previousPlanTitle = document.createElement("div")
    previousPlanTitle.innerHTML = "—— Previous Plan ——"
    previousPlanTitle.classList.add("plan-info-title")
    plans.append(previousPlanTitle)

    let previousPlan = ["Go to objective C", "a", "A", "a", "a", "a", "Acquire package #1", "Go to base"]
    previousPlan.forEach((description) => {
        let task = document.createElement("div")
        task.classList.add("plan-info-tag")
        task.style.backgroundColor = "peachpuff"
        task.innerHTML = description
        plans.append(task)
    });

}