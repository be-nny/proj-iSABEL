function linkClicked(name) {
    switch (name){
        case "leaderboard":
            sleep(500).then(() => {
                window.location.href = "leaderboard";
            });
            break;

        case "rewards":
            sleep(500).then(() => {
                window.location.href = "rewards";
            });
            break;

        case "scan":
            sleep(500).then(() => {
                window.location.href = "scan";
            });
            break;

        case "profile":
            sleep(500).then(() => {
                window.location.href = "profile";
            });
            break;

        case "about":
            sleep(500).then(() => {
                window.location.href = "about";
            });
            break;
    }
}

function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

function checkTabs(){
    var path = document.location.pathname;
    path = path.replace("/", "");
    if(path.includes("leaderboard")){
        document.getElementById("leaderboard").checked = true;

    } else if(path.includes("rewards")){
        document.getElementById("rewards").checked = true;

    } else if(path.includes("scan")){
        document.getElementById("scan").checked = true;

    }else if(path.includes("profile")){
        document.getElementById("profile").checked = true;

    }else if(path.includes("about")){
        document.getElementById("about").checked = true;
    }
}
