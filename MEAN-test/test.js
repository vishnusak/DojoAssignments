var app = angular.module('myApp', ['ngRoute'])

var count = 0,
    urlLink = ''

app.config(function($routeProvider){
  $routeProvider
  .when('/show',{
    templateUrl: '/testimg.html',
    controller: "testController"
  })
})

app.factory("urlfactory", function(){
  var factory = {},
      url = ''

  factory.getUrl = function(){
    return url
  }

  factory.setUrl = function(inpUrl){
    console.log("in setUrl");
    url = inpUrl
    console.log(url);
  }

  return factory
})

app.controller("main", ['$scope', 'urlfactory', function($scope, uf){
  $scope.urlLink = ''
  $scope.captureUrl = function(){
    uf.setUrl($scope.urlLink)
  }
}])

app.controller("testController", ['$scope', '$http', 'urlfactory', function($scope, $http, uf){
  console.log(`I am here in testController`);
  console.log(`inside testController: ${uf.getUrl()}`);
  $http({
    method: 'POST',
    url: '/show',
    data: {link: uf.getUrl()}
  }).then(function(serverData){
    // console.log(`Get AllServerData seccessful`)
    $scope.imgName = serverData.data
  })
}])
