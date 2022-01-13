// bulk operations start
vm.areAllRemoteJobsSelected = false;
vm.remoteJobsSelected = [];
vm.updateRemoteJobsSelection = updateRemoteJobsSelection;
vm.updateSelectedRemoteJobs = updateSelectedRemoteJobs;
vm.importRemoteJobs = importRemoteJobs;
vm.syncSelected = syncSelected;
vm.deleteSelected = deleteSelected;
vm.exportSelected = exportSelected;

function updateRemoteJobsSelection(remoteJobArray, selectionValue) {
    for (var i = 0; i < remoteJobArray.length; i++) {
        remoteJobArray[i].isSelected = selectionValue;
    }
    if (selectionValue === false) {
        vm.remoteJobsSelected = [];
    } else {
        vm.remoteJobsSelected = remoteJobArray;
    }
}

function updateSelectedRemoteJobs(remoteJob, selectionValue) {
    if (selectionValue === true) {
        vm.remoteJobsSelected.push(remoteJob);
    } else {
        vm.remoteJobsSelected.pop(remoteJob);
    }
}

function importRemoteJobs() {
    for (var i = 0; i < vm.remoteJobsSelected.length; i++) {
        var remoteJob = vm.remoteJobsSelected[i];
        if (remoteJob.isSelected) {
            //RemoteJob.update(remoteJob);
            //TODO: handle bulk export
        }
    }
}

function exportSelected() {
    for (var i = 0; i < vm.remoteJobsSelected.length; i++) {
        var remoteJob = vm.remoteJobsSelected[i];
        if (remoteJob.isSelected) {
            //RemoteJob.update(remoteJob);
            //TODO: handle bulk export
        }
    }
}

function deleteSelected() {
    for (var i = 0; i < vm.remoteJobsSelected.length; i++) {
        var remoteJob = vm.remoteJobsSelected[i];
        if (remoteJob.isSelected) {
            RemoteJob.delete(remoteJob);
        }
    }
}

function syncSelected() {
    for (var i = 0; i < vm.remoteJobsSelected.length; i++) {
        var remoteJob = vm.remoteJobsSelected[i];
        if (remoteJob.isSelected) {
            RemoteJob.update(remoteJob);
        }
    }
}

// <th><input type="checkbox" ng-model="vm.areAllRemoteJobsSelected" ng-change="vm.updateRemoteJobsSelection(vm.remoteJobs, vm.areAllRemoteJobsSelected)"/></th>

// <td><input type="checkbox" ng-change="vm.updateSelectedRemoteJobs(remoteJob, remoteJob.isSelected)" ng-model="remoteJob.isSelected"/></td>

// <div class="text-right">
//     <form name="searchForm" class="form-inline" ng-submit="vm.search(vm.searchQuery)" role="form"
// novalidate show-validation>
// <div class="input-group input-group-sm">
//     <input type="text" class="form-control" ng-model="vm.searchQuery"
// placeholder="Search for..." required/>
// <div class="input-group-btn">
//     <button ng-disabled="searchForm.$invalid" class="btn btn-info btn-raised"
// ng-click="vm.search(vm.searchQuery)">
//     <span class="glyphicon glyphicon-search"></span>
//     <span translate="entity.action.search">Search a RemoteJob</span>
// </button>
// <button class="btn btn-danger btn-raised" ng-click="vm.clear()"
// ng-if="vm.currentSearch">
//     <span class="glyphicon glyphicon-trash"></span>
//     <span translate="entity.action.clear">Clear</span>
//     </button>
//     <button ng-disabled="!vm.areAllRemoteJobsSelected && !vm.remoteJobsSelected.length"
// class="btn btn-raised btn-default" ng-click="vm.syncSelected()">
//     <i class="glyphicon glyphicon-refresh" aria-label="sync"></i>
//     <span translate="entity.action.sync">sync</span>
//     </button>
//     <button ng-disabled="!vm.areAllRemoteJobsSelected && !vm.remoteJobsSelected.length"
// class="btn btn-raised btn-default btn-danger"
// ng-click="vm.deleteSelected()">
//     <i class="glyphicon glyphicon-trash" aria-label="delete"></i> <span
// translate="entity.action.delete">delete</span>
//     </button>
//     <button ng-disabled="!vm.areAllRemoteJobsSelected && !vm.remoteJobsSelected.length"
// class="btn btn-raised btn-default" ng-click="vm.exportSelected()">
//     <i class="glyphicon glyphicon-export" aria-label="export"></i> <span
// translate="entity.action.export">export</span>
// </button>
// <button ng-disabled="vm.areAllRemoteJobsSelected && vm.remoteJobsSelected.length"
// class="btn btn-raised btn-default" ui-sref="remoteJob.import">
//     <i class="glyphicon glyphicon-import" aria-label="import"></i> <span
// translate="entity.action.import">import</span>
// </button>
// </div>
// </div>
// </form>
// </div>
