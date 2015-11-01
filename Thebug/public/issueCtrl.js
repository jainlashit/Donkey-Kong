routerApp.factory('issueFactory',function($http)
{
	var o = {};
	var result = [];
	var issues = [];
    var urlBase = "http://localhost:3000/issues";
	o.IssueExtractor = function($scope)
	{
		return $http.get(urlBase);
	}
    o.Delete = function(id)
    {
        return $http.delete(urlBase + '/' + id);
    }
    return o;
});

routerApp.controller('issueCtrl',function($scope,$http,issueFactory)
{
	issueFactory.IssueExtractor().success(function(data) {
        $scope.issues = angular.copy(data.issues);
        //console.log(data.issues);
        $scope.deleteIssue = function(id)
        {
            issueFactory.Delete(id).success(function()
            {
                issueFactory.IssueExtractor().success(function(data) {
                    $scope.issues = angular.copy(data.issues);
                });
            });
        }
	});
});
