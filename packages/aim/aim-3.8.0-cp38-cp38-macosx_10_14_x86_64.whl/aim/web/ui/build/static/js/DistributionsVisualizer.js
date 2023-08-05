(this.webpackJsonpui_v2=this.webpackJsonpui_v2||[]).push([[8],{1264:function(t,e,a){},1305:function(t,e,a){"use strict";a.r(e);var i=a(0),r=a.n(i),s=a(136),n=a(8),o=a(35),c=a(37),p=a(63),l=a(64),u=a(220),h=a(219),m=a(641),d=a.n(m),f=a(769),b=a.n(f),g=a(1262),v=a.n(g),x=a(1),y=function(t){Object(p.a)(a,t);var e=Object(l.a)(a);function a(t){var i;Object(o.a)(this,a);var s=[{type:"histogram",data:(i=e.call(this,t)).props.data,color:"#3E72E7",tooltip:{pointFormat:"Bin: <b>{point.x}</b> <br /> Frequency:  <b>{point.y}</b>"}}];return i.props.line&&s.push({type:"line",data:i.props.line,color:"rgb(28, 40, 82)",tooltip:{headerFormat:"",pointFormat:"Frequency: <b>{point.y}</b>"},marker:{enabled:!0,radius:2,fillColor:"#3b5896",lineWidth:1,lineColor:"rgb(28, 40, 82)",symbol:"circle"}}),i.state={options:{chart:{marginTop:70,marginBottom:50,spacing:[10,20,10,10],height:250},xAxis:{labels:{align:"center"}},yAxis:{title:{enabled:!1},tickWidth:1},title:{text:null},subtitle:{text:i.props.subtitle},credits:{enabled:!1},legend:{enabled:!1},series:s,plotOptions:{series:{states:{inactive:{opacity:1}}}}}},i.chartRef=r.a.createRef(),i}return Object(c.a)(a,[{key:"componentWillMount",value:function(){v()(d.a)}},{key:"componentDidUpdate",value:function(t){t.data!==this.props.data&&this.chartRef.current.chart.update({series:[{data:this.props.data.data},{line:this.props.data.line}]})}},{key:"render",value:function(){return Object(x.jsx)(b.a,{highcharts:d.a,options:this.state.options,ref:this.chartRef})}}]),a}(r.a.Component);y.defaultProps={subtitle:""};var j=y,O=a(17),k=a(1263),L=a.n(k),z=function(t){Object(p.a)(a,t);var e=Object(l.a)(a);function a(t){var r;return Object(o.a)(this,a),(r=e.call(this,t)).serializeData=function(t){return t.map((function(t){return 0!==r.props.max?[t[0],t[1],t[2]/r.props.max]:[t[0],t[1],0]}))},r.serializeY=function(){return r.props.y.map((function(t){return""+Math.round(1e4*t)/1e4}))},r.serializeX=function(){return r.props.x.map((function(t){return"".concat(t)}))},r.getPlotLines=function(t){return[{color:"#243969",width:2,value:t,zIndex:5}]},r.tooltipFormatter=function(){var t=r.props.max,e=Object(O.a)(r);return function(a){arguments.length>1&&void 0!==arguments[1]||this.x;var i=arguments.length>2&&void 0!==arguments[2]?arguments[2]:this.value;return"Step ".concat(e.props.iters[this.x],": <b>").concat(Math.round(i*t),"</b>")}},r.state={options:{chart:{type:"heatmap",marginTop:10,marginRight:80,height:180,spacing:[10,20,10,10]},credits:{enabled:!1},boost:{useGPUTranslations:!0},title:{text:null},subtitle:{text:null},xAxis:{categories:r.serializeX(),labels:{align:"center"},showLastLabel:!0,plotLines:r.getPlotLines(r.props.cursor)},yAxis:{categories:r.serializeY(),title:{enabled:!1},showLastLabel:!1,reversed:!0},legend:{align:"right",layout:"vertical",padding:0,margin:10,itemMarginTop:0,itemMarginBottom:0,verticalAlign:"center",symbolHeight:150},colorAxis:{stops:[[0,"#ffffff"],[.25,"#abcaf6"],[.5,"#77a8ef"],[.75,"#3578e6"],[1,"#225ae0"]],min:0,max:1},series:[{name:r.props.name,tooltip:{pointFormatter:r.tooltipFormatter()},data:r.serializeData(r.props.data),events:{click:r.props.click},dataLabels:{enabled:!1}}]}},r.chartRef=Object(i.createRef)(),r}return Object(c.a)(a,[{key:"componentWillMount",value:function(){L()(d.a)}},{key:"componentDidUpdate",value:function(t){if(t.x!==this.props.x&&this.chartRef.current.chart.update({xAxis:{categories:this.serializeX()}}),t.y!==this.props.y&&this.chartRef.current.chart.update({yAxis:{categories:this.serializeY()}}),t.data===this.props.data&&t.max===this.props.max||this.chartRef.current.chart.series[0].update({data:this.serializeData(this.props.data),tooltip:{pointFormatter:this.tooltipFormatter()}}),t.cursor!==this.props.cursor){var e=Object.assign({},this.state.xAxis);e.plotLines=this.getPlotLines(this.props.cursor),this.chartRef.current.chart.update({xAxis:e})}}},{key:"render",value:function(){return Object(x.jsx)(b.a,{highcharts:d.a,options:this.state.options,ref:this.chartRef})}}]),a}(i.Component);z.defaultProps={name:"Series",min:0};var D=z,M=function(t){Object(p.a)(a,t);var e=Object(l.a)(a);function a(t){var i;return Object(o.a)(this,a),(i=e.call(this,t)).computeHeatmap=function(){i.props.data.length?i.setState({histogram:[],histogramLine:[],heatmapX:[],heatmapY:[],heatmapValMax:null,heatmapData:[],cursor:-1},(function(){var t=i.props.data,e=null,a=null,r=null;t.forEach((function(t){var i=t[1];(null==e||i[0]<e)&&(e=i[0]),(null==a||i[i.length-1]>a)&&(a=i[i.length-1])}));for(var s={},n=[],o=[],c=[],p=(a-e)/20,l=0;l<i.props.data.length;l++)o.push("".concat(i.props.iters[l]));for(var u=e;u<=a;u+=p)c.push("".concat(u));t.forEach((function(t,e){t[0].forEach((function(a,i){for(var r=0,n=1;n<c.length;n++)if(r=n,parseFloat(c[n])>t[1][i]){r--;break}var p=o.length*r+e;void 0===s[p]&&(s[p]=[]),s[p].push(a)}))}));for(var h=0;h<o.length*c.length;h++)void 0===s[h]&&(s[h]=[0]);for(var m in s){var d=Math.floor(m/o.length),f=m%o.length,b=s[m].reduce((function(t,e){return t+e}));(null==r||b>r)&&(r=b),n.push([f,d,b])}i.setState({heatmapY:c,heatmapX:o,heatmapValMax:r,heatmapData:n,empty:!1,key:i.props.name}),i.computeHistogram(0)})):i.setState({empty:!0})},i.computeHistogram=function(t){var e=i.props.data;if(!(t>=e.length||i.state.cursor===t)){var a=e[t][0].map((function(a,i){return[e[t][1][i],a]})),r=e[t][0].map((function(a,i){return[(e[t][1][i]+e[t][1][i+1])/2,a]}));i.setState({histogram:a,histogramLine:r,cursor:t})}},i.handleClick=function(t){i.computeHistogram(t.point.x),Object(h.b)(u.a.runDetails.tabs.distributions.onClickHeatMapCell)},i.state={empty:!0,key:Math.random()},i}return Object(c.a)(a,[{key:"componentDidMount",value:function(){this.computeHeatmap()}},{key:"componentDidUpdate",value:function(t){t.data!==this.props.data&&this.computeHeatmap(),t.name!==this.props.name&&this.computeHeatmap()}},{key:"render",value:function(){var t=this;return!this.state.empty&&Object(x.jsxs)("div",{className:"Charts",style:{width:"100%"},children:[Object(x.jsx)(j,{data:this.state.histogram,line:this.state.histogramLine,subtitle:"Step ".concat(this.props.iters[this.state.cursor])},this.state.cursor),Object(x.jsx)(D,{x:this.state.heatmapX,y:this.state.heatmapY,max:this.state.heatmapValMax,data:this.state.heatmapData,cursor:this.state.cursor,name:"Frequency",click:function(e){return t.handleClick(e)},iters:this.props.iters})]},this.state.key)}}]),a}(r.a.Component);a(1264);function F(t){var e,a;return Object(x.jsx)(n.a,{children:Object(x.jsx)(s.a,{className:"VisualizationLoader",isLoading:!!t.isLoading,children:Object(x.jsx)("div",{className:"DistributionsVisualizer",children:(null===(e=t.data)||void 0===e?void 0:e.processedValues)&&Object(x.jsx)(M,{data:null===(a=t.data)||void 0===a?void 0:a.processedValues,className:"Visualizer",iters:t.data.iters})})})})}F.displayName="DistributionsVisualizer";var R=Object(i.memo)(F);e.default=R}}]);
//# sourceMappingURL=DistributionsVisualizer.js.map?version=419490ff9e5d387aa954