(this.webpackJsonpui_v2=this.webpackJsonpui_v2||[]).push([[18],{1137:function(e,t,a){},1138:function(e,t,a){},1139:function(e,t,a){},1140:function(e,t,a){},1141:function(e,t,a){},1142:function(e,t,a){},1294:function(e,t,a){"use strict";a.r(t);var n,i=a(0),c=a.n(i),r=a(8),s=a(220),o=a(244),l=a(3),m=a(44),d=a.n(m),u=a(237),j=a(225),p=a(223),b=a(239),h=a(246),x=a(236),v=a(241),g=Object(v.a)({});function f(){var e=j.a.fetchActivityData(),t=e.call;return{call:function(){return t((function(e){Object(p.a)({detail:e,model:g})})).then((function(e){g.setState({activityData:e})}))},abort:e.abort}}var y=Object(l.a)(Object(l.a)({},g),{},{destroy:function(){g.destroy(),n.abort()},initialize:function(){g.init(),n=f();try{n.call((function(e){Object(p.a)({detail:e,model:g})}))}catch(t){Object(b.a)({notification:{messages:[t.message],severity:"error",id:Date.now()},model:g})}var e="true"===Object(x.a)("askEmailSent");g.setState({askEmailSent:e})},getActivityData:f,onSendEmail:function(e){return fetch("https://formspree.io/f/xeqvdval",{method:"Post",headers:{"Content-Type":"application/json"},body:JSON.stringify(e)}).then(function(){var e=Object(u.a)(d.a.mark((function e(t){return d.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,t.json();case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()).then((function(e){return e.ok?(Object(b.a)({notification:{severity:"success",messages:["Email Successfully sent"],id:Date.now()},model:g}),g.setState({askEmailSent:!0}),Object(x.b)("askEmailSent",!0)):Object(b.a)({notification:{severity:"error",messages:["Please enter valid email"],id:Date.now()},model:g}),e}))},onHomeNotificationDelete:function(e){Object(h.a)({model:g,id:e})}}),_=a(219),N=a(486),S=a.p+"static/media/github.a1af1e77.svg",w=a.p+"static/media/slack.2d5fba05.svg",D=a(4),C=a(166),z=(a(1137),a(1));function k(e){var t=e.title,a=e.path,n=e.description,i=e.icon;return Object(z.jsx)(r.a,{children:Object(z.jsxs)(C.c,{className:"ExploreAimCard",to:"/".concat(a),children:[Object(z.jsx)("div",{className:"ExploreAimCard__icon",children:Object(z.jsx)(D.g,{name:"".concat(i)})}),Object(z.jsx)(D.m,{component:"h4",weight:600,size:16,className:"ExploreAimCard__title",tint:100,children:t}),Object(z.jsx)(D.m,{component:"span",weight:400,size:14,className:"ExploreAimCard__desc",tint:100,children:n}),Object(z.jsx)("div",{className:"ExploreAimCard__arrow__icon",children:Object(z.jsx)(D.g,{name:"long-arrow-right"})})]})})}var E=c.a.memo(k),M=(a(1138),[{title:"Runs Explorer",description:"View all your runs holistically on Runs Explorer: all hyperparameters, all metric last values",path:"runs",icon:"runs"},{title:"Metrics Explorer",description:"Compare 100s of metrics in a few clicks on Metrics Explorer",path:"metrics",icon:"metrics"},{title:"Images Explorer",description:"Track intermediate images and search, compare them on Images Explorer",path:"images",icon:"images"},{title:"Params Explorer",description:"The Params explorer enables a parallel coordinates view for metrics and params",path:"params",icon:"params"},{title:"Scatters Explorer",description:"Explore and learn relationship, correlations, and clustering effects between metrics and parameters on Scatters Explorer",path:"scatters",icon:"scatterplot"}]);function O(){return Object(z.jsx)(r.a,{children:Object(z.jsxs)("div",{className:"ExploreAim",children:[Object(z.jsxs)("div",{children:[Object(z.jsx)(D.m,{component:"h2",tint:100,weight:600,size:24,children:"Get Involved"}),Object(z.jsxs)("div",{className:"ExploreAim__social",children:[Object(z.jsxs)("a",{target:"_blank",href:"https://slack.aimstack.io",rel:"noreferrer",className:"ExploreAim__social__item",onClick:function(){return Object(_.b)(s.a.home.slackCommunity)},children:[Object(z.jsx)("img",{src:w,alt:"slack"}),Object(z.jsx)(D.m,{component:"span",tint:100,size:16,weight:500,children:"Join Aim slack community"}),Object(z.jsx)(D.g,{name:"arrow-right"})]}),Object(z.jsxs)("a",{target:"_blank",href:"https://github.com/aimhubio/aim",rel:"noreferrer",className:"ExploreAim__social__item",onClick:function(){return Object(_.b)(s.a.home.createGithubIssue)},children:[Object(z.jsx)("img",{src:S,alt:"github"}),Object(z.jsxs)(D.m,{component:"span",tint:100,size:16,weight:500,children:["Create an issue ",Object(z.jsx)("br",{})," or report a bug to help us improve"]}),Object(z.jsx)(D.g,{name:"arrow-right"})]})]})]}),Object(z.jsxs)("div",{className:"ExploreAim__block__item",children:[Object(z.jsx)(D.m,{component:"h2",tint:100,weight:600,size:24,children:"Explore Aim"}),Object(z.jsx)("div",{className:"ExploreAim__card__container",children:M.map((function(e){return Object(z.jsx)(E,Object(l.a)({},e),e.path)}))})]})]})})}var B=c.a.memo(O),Y=a(621);a(1139);function H(e){e.askEmailSent,e.onSendEmail;return Object(z.jsx)(r.a,{children:Object(z.jsxs)("div",{className:"SetupGuide__container",children:[Object(z.jsx)(D.m,{component:"h2",size:24,weight:600,tint:100,children:"Integrate Aim with your code"}),Object(z.jsxs)("div",{className:"SetupGuide__code",children:[Object(z.jsx)(D.m,{component:"h3",size:18,tint:100,weight:600,children:"1. Import Aim"}),Object(z.jsx)(Y.a,{code:"import aim"})]}),Object(z.jsxs)("div",{className:"SetupGuide__code",children:[Object(z.jsx)(D.m,{component:"h3",size:18,tint:100,weight:600,children:"2. Track your training runs"}),Object(z.jsx)(Y.a,{code:"run_inst = aim.Run(experiment='my_exp_name')\n\n# Save inputs, hparams or any other `key: value` pairs\nrun_inst['hparams'] = {\n    'learning_rate': 0.01,\n    'batch_size': 32,\n}\n\n# Track metrics\nfor step in range(10):\n    run_inst.track(metric_value, name='metric_name', epoch=epoch_number)\n"})]}),Object(z.jsxs)("div",{className:"SetupGuide__resources__container",children:[Object(z.jsxs)("a",{target:"_blank",href:"https://aimstack.readthedocs.io/en/stable/",rel:"noreferrer",className:"SetupGuide__resources__item",onClick:function(){return Object(_.b)(s.a.home.docs)},children:[Object(z.jsx)("div",{className:"SetupGuide__resources__item__icon",children:Object(z.jsx)(D.g,{className:"SetupGuide__resources__item__icon_fullDocs",name:"full-docs"})}),Object(z.jsx)(D.m,{component:"span",size:14,tint:100,weight:500,children:"Documentation"})]}),Object(z.jsx)("div",{className:"SetupGuide__resources__item",children:Object(z.jsxs)("a",{target:"_blank",href:"https://colab.research.google.com/drive/14rIAjpEyklf5fSMiRbyZs6iYG7IVibcI?usp=sharing",rel:"noreferrer",className:"SetupGuide__resources__item",onClick:function(){return Object(_.b)(s.a.home.colab)},children:[Object(z.jsx)("div",{className:"SetupGuide__resources__item__icon",children:Object(z.jsx)(D.g,{className:"SetupGuide__resources__item__icon_co",name:"co"})}),Object(z.jsx)(D.m,{component:"span",size:14,tint:100,weight:500,children:"Colab notebook"})]})}),Object(z.jsx)("div",{className:"SetupGuide__resources__item",children:Object(z.jsxs)("a",{target:"_blank",href:"http://play.aimstack.io:10001/metrics?grouping=8uYPXatSfU5QSDNPAu7p86Uw438qTupoLaxzkERnqPAfSSDTAANjKUXKghaTQgcdkgJu1DgEg9A3X61eePdqmTtkqrEmHHDvuSLjG8C44X3FNd1fdgx7nEsAm3wiQBDg1gjmFdZfvaf4qmbqxC6fp92DnDnjfw6KN4fqG3dr6QKRbMhqk6ThR2rsbVHAoFofbmyc2DqH35ZRKFZiEEdgUFVov6zVEDkW8MVvBJgw36iEvwBNhDrGD9zozbJhm5uz4NNjXdvaikfTVXgmgYM7oHVeM28Ci63bykQSt372tiZ8hXSjMUUbr9ipXna19ivDKKYKDcBsih3STFRprR278pMw3cd9AypyxxyQoLgqLFYwVN94tURTNrtEyJPQeQWYfjtKfEx2fLEVHHvZSWjBFHCHeN4FGpFwBx6bzpJcpSphG66StebxKq8j4gX4RvpVgXoGXMua35yj3SuDhJ&chart=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&select=7zY8cjozbtZPcd218aSeA6iwCEGaLqsuegewPXMXmDAtEKdrvzLb3u4zxJTbtBqNCKiG8wY9gzhgqiMsGcEcU2gWnt4PxCiKoV4qj2M3LRUKiEt7aVgC1qPzxsq8njZjLTD5MTxtLS69ZnAA4D89GE9Ck5BkwbhMedCpKiZdmxHDQ8owyFkVBXWETwPEC1K2tsqWv8fbCqf9kxZTELr8dfT1SLhzfsxvdcG2dBdaVJhAZahhZfkPY1b5urf2yWW4ynKzxeHYejJqgWSNiUzXXJGNtCXbYUkJ59higJEQdcY1JriFymBepjpV1BvZmmy6u2SXa4DoLWrgYSdwL3hqELPpDe1xvv7YLFEitKqmsYwvqfeysgL3Hn9FRRbwTDDibGBNQgrg9XsLxqnuWhkKaVJ3J1hETKMcydbCTUqTqsKbvKmZwoREXkyivQf6H75Y3jYZx33JjzkFEb9ZYcUYHQSwF5kMKPQhwRRGkbGMCZYqtokK59adpSy565E",rel:"noreferrer",className:"SetupGuide__resources__item",onClick:function(){return Object(_.b)(s.a.home.liveDemo)},children:[Object(z.jsx)("div",{className:"SetupGuide__resources__item__icon",children:Object(z.jsx)(D.g,{className:"SetupGuide__resources__item__icon_liveDemo",name:"live-demo"})}),Object(z.jsx)(D.m,{component:"span",size:14,tint:100,weight:500,children:"Live demo"})]})})]})]})})}var R=c.a.memo(H),W=a(560),G=a(390),T=a(25),V=a(56),A=a(450),X=a(463),F=(a(1140),[0,1,2,3,4]);var q=function(e){var t=e.data,a=e.startDate,n=e.endDate,i=e.cellSize,c=void 0===i?12:i,o=e.cellSpacing,l=void 0===o?4:o,m=e.scaleRange,d=void 0===m?4:m,u=e.onCellClick,j=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],p=Object(V.g)();a=new Date(a.getFullYear(),a.getMonth(),a.getDate()),n=new Date(n.getFullYear(),n.getMonth(),n.getDate());for(var b=a;0!==b.getDay();)b=N(b,-1);for(var h=n;0!==h.getDay();)h=N(h,1);0===h.getDay()&&(h=N(h,7));var x=Math.floor(Math.abs((b-h)/864e5)),v=Math.max.apply(Math,Object(T.a)(null===t||void 0===t?void 0:t.map((function(e){return null===e||void 0===e?void 0:e[1]})).filter((function(e){return Number.isInteger(e)})))),g=[].concat(Object(T.a)(j.slice(b.getMonth())),Object(T.a)(j.slice(0,b.getMonth()))),f={width:"".concat(x/7*c+(x/7-1)*l-50,"px")},y={gridTemplateColumns:"repeat(".concat(x/7,", 1fr)"),gridTemplateRows:"repeat(7, 1fr)",width:"".concat(x/7*c+(x/7-1)*l,"px"),height:"".concat(7*c+6*l,"px"),gridColumnGap:"".concat(l,"px"),gridRowGap:"".concat(l,"px")};function N(e,t){var a=new Date(e);return a.setDate(a.getDate()+t),a}function S(e){var t=Math.floor(e/7);return N(b,7*t+e%7)}function w(e){var a,i=function(e){for(var a=S(e),n=null,i=0;i<t.length;i++){var c,r,s;if((null===(c=t[i])||void 0===c?void 0:c[0].getFullYear())===a.getFullYear()&&(null===(r=t[i])||void 0===r?void 0:r[0].getMonth())===a.getMonth()&&(null===(s=t[i])||void 0===s?void 0:s[0].getDate())===a.getDate()){n=t[i];break}}return n}(e),c=S(e),o=i&&Number.isInteger(null===i||void 0===i?void 0:i[1])?(a=i[1],Math.ceil(a/v*d)):0,l=" ".concat(i?i[1]:0," tracked run").concat(1!==(null===i||void 0===i?void 0:i[1])?"s":""," on ").concat(j[c.getMonth()]," ").concat(c.getDate(),", ").concat(c.getFullYear());return Object(z.jsx)(r.a,{children:Object(z.jsx)("div",{className:"CalendarHeatmap__cell__wrapper",children:+n<+S(e)?Object(z.jsx)("div",{className:"CalendarHeatmap__cell CalendarHeatmap__cell--dummy"}):Object(z.jsx)(A.a,{title:l,children:Object(z.jsx)("div",{className:"CalendarHeatmap__cell CalendarHeatmap__cell--scale-".concat(o),onClick:function(e){if(e.stopPropagation(),u(),o){var t=c.getTime(),a=new Date(c.getFullYear(),c.getMonth(),c.getDate(),23,59,59).getTime(),n=Object(X.b)({query:"run.creation_time >= ".concat(t/1e3," and run.creation_time <= ").concat(a/1e3)});_.b(s.a.home.activityCellClick),p.push("/runs?select=".concat(n))}},role:"navigation"})})})},e)}return Object(z.jsxs)("div",{className:"CalendarHeatmap",children:[Object(z.jsxs)("div",{className:"CalendarHeatmap__map",children:[Object(z.jsx)("div",{}),Object(z.jsx)("div",{className:"CalendarHeatmap__map__axis CalendarHeatmap__map__axis--x",style:f,children:g.slice(0,10).map((function(e,t){return Object(z.jsx)("div",{className:"CalendarHeatmap__map__axis__tick--x",children:e},t)}))}),Object(z.jsx)("div",{className:"CalendarHeatmap__map__axis CalendarHeatmap__map__axis--y",children:["S","M","T","W","T","F","S"].map((function(e,t){return Object(z.jsx)("div",{className:"CalendarHeatmap__map__axis__tick--y",children:e},t)}))}),Object(z.jsx)("div",{className:"CalendarHeatmap__map__grid",style:y,children:Object(T.a)(Array(x).keys()).map((function(e){return w(e)}))})]}),Object(z.jsxs)("div",{className:"CalendarHeatmap__cell__info",children:[Object(z.jsx)(D.m,{weight:400,size:12,children:"Less"}),F.map((function(e){return Object(z.jsx)("div",{style:{width:c,height:c},className:"CalendarHeatmap__cell__wrapper",children:Object(z.jsx)("div",{className:"CalendarHeatmap__cell CalendarHeatmap__cell--scale-".concat(e)})},e)})),Object(z.jsx)(D.m,{weight:400,size:12,children:"More"})]})]})};a(1141);function J(e){var t,a,n,i=e.activityData;var c=new Date;return Object(z.jsx)(r.a,{children:Object(z.jsxs)(W.a,{className:"Activity",container:!0,spacing:1,children:[Object(z.jsxs)(W.a,{item:!0,children:[Object(z.jsx)(D.m,{component:"h2",size:24,weight:600,tint:100,children:"Statistics"}),Object(z.jsxs)("div",{className:"Activity__Statistics__card",children:[Object(z.jsx)(D.m,{size:16,component:"span",color:"secondary",children:"Experiments"}),Object(z.jsx)(D.m,{component:"strong",size:36,weight:600,color:"secondary",children:null!==(t=null===i||void 0===i?void 0:i.num_experiments)&&void 0!==t?t:Object(z.jsx)(G.a,{className:"Activity__loader"})})]}),Object(z.jsxs)("div",{className:"Activity__Statistics__card",children:[Object(z.jsx)(D.m,{size:16,component:"span",color:"secondary",children:"Runs"}),Object(z.jsx)(D.m,{component:"strong",size:36,weight:600,color:"secondary",children:null!==(a=null===i||void 0===i?void 0:i.num_runs)&&void 0!==a?a:Object(z.jsx)(G.a,{className:"Activity__loader"})})]})]}),Object(z.jsxs)(W.a,{xs:!0,item:!0,children:[Object(z.jsx)(D.m,{component:"h2",size:24,weight:600,tint:100,children:"Activity"}),Object(z.jsx)("div",{className:"Activity__HeatMap",children:Object(z.jsx)(q,{startDate:function(e,t){var a=new Date(e);return a.setDate(a.getDate()+t),a}(c,-300),endDate:c,onCellClick:function(){Object(_.b)(s.a.home.activityCellClick)},data:Object.keys(null!==(n=null===i||void 0===i?void 0:i.activity_map)&&void 0!==n?n:{}).map((function(e){return[new Date(e),i.activity_map[e]]}))})})]})]})})}var K=c.a.memo(J);a(1142);var L=function(e){var t=e.activityData,a=e.onSendEmail,n=e.notifyData,i=e.onNotificationDelete,c=e.askEmailSent;return Object(z.jsx)(r.a,{children:Object(z.jsxs)("section",{className:"Home__container",children:[Object(z.jsx)("div",{className:"Home__Activity__container",children:Object(z.jsx)(K,{activityData:t})}),Object(z.jsxs)("div",{className:"Home__Explore__container",children:[Object(z.jsx)(R,{askEmailSent:c,onSendEmail:a}),Object(z.jsx)(B,{})]}),(null===n||void 0===n?void 0:n.length)>0&&Object(z.jsx)(N.a,{handleClose:i,data:n})]})})};t.default=function(){var e=Object(o.a)(y);return c.a.useEffect((function(){return y.initialize(),_.b(s.a.home.pageView),function(){y.destroy()}}),[]),Object(z.jsx)(r.a,{children:Object(z.jsx)(L,{onSendEmail:y.onSendEmail,activityData:e.activityData,notifyData:e.notifyData,askEmailSent:e.askEmailSent,onNotificationDelete:y.onHomeNotificationDelete})})}},463:function(e,t,a){"use strict";(function(e){a.d(t,"b",(function(){return s})),a.d(t,"a",(function(){return o}));var n=a(532),i=a.n(n),c=a(550),r=a.n(c);function s(t,a){return a?r()(JSON.stringify(t)):i.a.encode(e.from(JSON.stringify(t)))}function o(e){try{return i.a.decode(e).toString()}catch(t){return"{}"}}}).call(this,a(474).Buffer)},483:function(e,t,a){},486:function(e,t,a){"use strict";a.d(t,"a",(function(){return m}));a(0);var n=a(1304),i=a(1307),c=a(1311),r=a.p+"static/media/successIcon.bd3fad23.svg",s=a.p+"static/media/errorIcon.09cae82c.svg",o=a(8),l=(a(483),a(1));function m(e){var t=e.data,a=e.handleClose;return Object(l.jsx)(o.a,{children:Object(l.jsx)("div",{children:Object(l.jsx)(i.a,{open:!0,autoHideDuration:3e3,anchorOrigin:{vertical:"top",horizontal:"right"},children:Object(l.jsx)("div",{className:"NotificationContainer",children:t.map((function(e){var t=e.id,i=e.severity,o=e.messages;return Object(l.jsx)(c.a,{mt:.5,children:Object(l.jsx)(n.a,{onClose:function(){return a(+t)},variant:"outlined",severity:i,iconMapping:{success:Object(l.jsx)("img",{src:r,alt:""}),error:Object(l.jsx)("img",{src:s,alt:""})},style:{height:"auto"},children:Object(l.jsxs)("div",{className:"NotificationContainer__contentBox",children:[Object(l.jsx)("p",{className:"NotificationContainer__contentBox__severity",children:i}),o.map((function(e,t){return e?Object(l.jsx)("p",{className:"NotificationContainer__contentBox__message",children:e},t):null}))]})})},t)}))})})})})}},545:function(e,t){},546:function(e,t){},547:function(e,t){},548:function(e,t){},560:function(e,t,a){"use strict";var n=a(5),i=a(2),c=a(0),r=(a(15),a(6)),s=a(13),o=[0,1,2,3,4,5,6,7,8,9,10],l=["auto",!0,1,2,3,4,5,6,7,8,9,10,11,12];function m(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:1,a=parseFloat(e);return"".concat(a/t).concat(String(e).replace(String(a),"")||"px")}var d=c.forwardRef((function(e,t){var a=e.alignContent,s=void 0===a?"stretch":a,o=e.alignItems,l=void 0===o?"stretch":o,m=e.classes,d=e.className,u=e.component,j=void 0===u?"div":u,p=e.container,b=void 0!==p&&p,h=e.direction,x=void 0===h?"row":h,v=e.item,g=void 0!==v&&v,f=e.justify,y=e.justifyContent,_=void 0===y?"flex-start":y,N=e.lg,S=void 0!==N&&N,w=e.md,D=void 0!==w&&w,C=e.sm,z=void 0!==C&&C,k=e.spacing,E=void 0===k?0:k,M=e.wrap,O=void 0===M?"wrap":M,B=e.xl,Y=void 0!==B&&B,H=e.xs,R=void 0!==H&&H,W=e.zeroMinWidth,G=void 0!==W&&W,T=Object(n.a)(e,["alignContent","alignItems","classes","className","component","container","direction","item","justify","justifyContent","lg","md","sm","spacing","wrap","xl","xs","zeroMinWidth"]),V=Object(r.a)(m.root,d,b&&[m.container,0!==E&&m["spacing-xs-".concat(String(E))]],g&&m.item,G&&m.zeroMinWidth,"row"!==x&&m["direction-xs-".concat(String(x))],"wrap"!==O&&m["wrap-xs-".concat(String(O))],"stretch"!==l&&m["align-items-xs-".concat(String(l))],"stretch"!==s&&m["align-content-xs-".concat(String(s))],"flex-start"!==(f||_)&&m["justify-content-xs-".concat(String(f||_))],!1!==R&&m["grid-xs-".concat(String(R))],!1!==z&&m["grid-sm-".concat(String(z))],!1!==D&&m["grid-md-".concat(String(D))],!1!==S&&m["grid-lg-".concat(String(S))],!1!==Y&&m["grid-xl-".concat(String(Y))]);return c.createElement(j,Object(i.a)({className:V,ref:t},T))})),u=Object(s.a)((function(e){return Object(i.a)({root:{},container:{boxSizing:"border-box",display:"flex",flexWrap:"wrap",width:"100%"},item:{boxSizing:"border-box",margin:"0"},zeroMinWidth:{minWidth:0},"direction-xs-column":{flexDirection:"column"},"direction-xs-column-reverse":{flexDirection:"column-reverse"},"direction-xs-row-reverse":{flexDirection:"row-reverse"},"wrap-xs-nowrap":{flexWrap:"nowrap"},"wrap-xs-wrap-reverse":{flexWrap:"wrap-reverse"},"align-items-xs-center":{alignItems:"center"},"align-items-xs-flex-start":{alignItems:"flex-start"},"align-items-xs-flex-end":{alignItems:"flex-end"},"align-items-xs-baseline":{alignItems:"baseline"},"align-content-xs-center":{alignContent:"center"},"align-content-xs-flex-start":{alignContent:"flex-start"},"align-content-xs-flex-end":{alignContent:"flex-end"},"align-content-xs-space-between":{alignContent:"space-between"},"align-content-xs-space-around":{alignContent:"space-around"},"justify-content-xs-center":{justifyContent:"center"},"justify-content-xs-flex-end":{justifyContent:"flex-end"},"justify-content-xs-space-between":{justifyContent:"space-between"},"justify-content-xs-space-around":{justifyContent:"space-around"},"justify-content-xs-space-evenly":{justifyContent:"space-evenly"}},function(e,t){var a={};return o.forEach((function(n){var i=e.spacing(n);0!==i&&(a["spacing-".concat(t,"-").concat(n)]={margin:"-".concat(m(i,2)),width:"calc(100% + ".concat(m(i),")"),"& > $item":{padding:m(i,2)}})})),a}(e,"xs"),e.breakpoints.keys.reduce((function(t,a){return function(e,t,a){var n={};l.forEach((function(e){var t="grid-".concat(a,"-").concat(e);if(!0!==e)if("auto"!==e){var i="".concat(Math.round(e/12*1e8)/1e6,"%");n[t]={flexBasis:i,flexGrow:0,maxWidth:i}}else n[t]={flexBasis:"auto",flexGrow:0,maxWidth:"none"};else n[t]={flexBasis:0,flexGrow:1,maxWidth:"100%"}})),"xs"===a?Object(i.a)(e,n):e[t.breakpoints.up(a)]=n}(t,e,a),t}),{}))}),{name:"MuiGrid"})(d);t.a=u},600:function(e,t,a){},621:function(e,t,a){"use strict";var n=a(3),i=a(0),c=a.n(i),r=a(712),s=a(666),o=a(9),l=a(4),m=a(8),d=a(1);function u(e){var t=e.contentRef,a=e.showSuccessDelay,n=void 0===a?1500:a,i=e.className,r=void 0===i?"":i,s=c.a.useState(!1),u=Object(o.a)(s,2),j=u[0],p=u[1];c.a.useEffect((function(){j&&setTimeout((function(){p(!1)}),n)}),[j]);var b=c.a.useCallback((function(){t.current&&!j&&navigator.clipboard.writeText(t.current.innerText.trim("")).then((function(){p(!0)})).catch()}),[t,j]);return Object(d.jsx)(m.a,{children:Object(d.jsx)("span",{className:r,onClick:b,children:j?Object(d.jsx)("span",{style:{color:"green",fontSize:12},children:"Copied!"}):Object(d.jsx)(l.g,{name:"copy"})})})}u.displayName="CopyToClipBoard";var j=c.a.memo(u);a(600);function p(e){var t=e.code,a=void 0===t?"":t,i=e.className,o=void 0===i?"":i,l=e.language,u=void 0===l?"python":l,p=c.a.createRef();return Object(d.jsx)(m.a,{children:Object(d.jsxs)("div",{className:"CodeBlock ".concat(o),children:[Object(d.jsx)(r.a,Object(n.a)(Object(n.a)({},r.b),{},{theme:s.a,code:a.trim(),language:u,children:function(e){var t=e.className,a=e.style,i=e.tokens,c=e.getLineProps,r=e.getTokenProps;return Object(d.jsx)("pre",{className:t,style:a,ref:p,children:i.map((function(e,t){return Object(d.jsx)("div",Object(n.a)(Object(n.a)({},c({line:e,key:t})),{},{children:e.map((function(e,t){return Object(d.jsx)("span",Object(n.a)({},r({token:e,key:t})),t)}))}),t)}))})}})),Object(d.jsx)(m.a,{children:Object(d.jsx)(j,{className:"CodeBlock__copy__span",contentRef:p})})]})})}t.a=c.a.memo(p)}}]);
//# sourceMappingURL=home.js.map?version=252eec4efd2b57ee2289