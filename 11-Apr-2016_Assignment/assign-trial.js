$('document').ready(function(){
//   // function header(){
//   //   $('header').slideDown(1000);
//   // }

//   // function sides(){
//   //   $('.back').animate({width: "5%"},1000);
//   //   $('.fwd').animate({width: "5%"},1000);
//   // }

//   // function showsides(){
//   //   $('.back, .fwd').css("color", "navy");
//   // }

//   // header(); 

//   $('header').slideDown(1000);
//   $('header').promise().done(function(){
//     $('.back').animate({width: "5%"},1000);
//     $('.fwd').animate({width: "5%"},1000);
//     $('.fwd').promise().done(function(){
//       $('.fwd, .back').css("color", "navy");
//       $('fwd').promise().done(function(){
//         $('#c1').fadeIn(5000);
//       })
//     })
//   });

//   function next(cDiv, nDiv){
//     $(cDiv).fadeOut(1000);
//     $(cDiv).promise().done(function(){
//       $(nDiv).show().animate({width:'100%'}, 1000);
//     })
//   }
//   var fwd = 1;
//   var bck = 6;

//   $('.fwd').click(function(){
//     // $('.challenge').hide();
//     fwd++;
//     switch (fwd){
//       case 1:
//         bck = 6;
//         $('#c1').show();
//         break;
//       case 2:
//         bck = fwd;
//         next('#c1', '#c2');
//         // $('#c2').show();
//         break;
//       case 3:
//         bck = fwd;
//         $('#c3').show();
//         break;
//       case 4:
//         bck = fwd;
//         $('#c4').show();
//         break;
//       case 5:
//         bck = fwd;
//         $('#c5').show();
//         fwd = 0;
//         break;
//     }
//   })

//   $('.back').click(function(){
//     $('.challenge').hide();
//     bck--;
//     switch (bck){
//       case 1:
//         fwd = bck;
//         $('#c1').show();
//         bck = 6;
//         break;
//       case 2:
//         fwd = bck;
//         $('#c2').show();
//         break;
//       case 3:
//         fwd = bck;
//         $('#c3').show();
//         break;
//       case 4:
//         fwd = bck;
//         $('#c4').show();
//         break;
//       case 5:
//         $('#c5').show();
//         fwd = 0;
//         break;
//     }
//   })
})