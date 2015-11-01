routerApp.controller('createCtrl',function($scope,$http)
{
	$scope.insert_project = function(value)
	{
		var promise = $http.post("http://localhost:3000/projects/", {
			"project": {
					"creator":$scope.project_creator,
					"name":$scope.project_name,
					"is_public":value,
				}
		});

		promise.success(function(data,status,header,config) {
			console.log("Project Created");
		});
	};	
});