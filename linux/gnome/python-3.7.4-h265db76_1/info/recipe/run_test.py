teElement("div",{key:500,className:"homepageFeaturedArticleSlider noSlide"},a.createPredictorSection())):e>7&&t.push(o.default.createElement("div",{key:100,className:"sliderContainer homepageFeaturedArticleSlider"},o.default.createElement(l.default,{dots:!1,infinite:!0,speed:500,slidesToShow:6,slidesToScroll:1,autoplay:!1}," ",a.createPredictorSection()," "))),t},a}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,r.Component),n(t,[{key:"createPredictorSection",value:function(){var e=this,t=this.props.predictorData,a=t.basecourseCounts,n=t.streamCounts,r=[];return void 0!==s.predictorList&&Object.keys(s.predictorList).forEach(function(t,o){o<=9&&("baseCourse"==s.predictorList[t].entityType?r.push(e.getPredictorItems(s.predictorList[t].entityId,s.predictorList[t].label,a[s.predictorList[t].entityId],s.predictorList[t].thumbUrl,s.predictorList[t].form2Url,o)):"stream"==s.predictorList[t].entityType&&r.push(e.getPredictorItems(s.predictorList[t].entityId,s.predictorList[t].label,n[s.predictorList[t].entityId],s.predictorList[t].thumbUrl,s.predictorList[t].form2Url,o)))}),r}},{key:"getPredictorItems",value:function(e,t,a,n,r,l){var s=a>1?a+" Exams":1==a?a+" Exam":"";return o.default.createElement("div",{className:"slideItem",key:l},o.default.createElement("div",null,o.default.createElement(c.default,{className:"predictorBox",to:r,lang:"en"},o.default.createElement("span",null,o.default.createElement(i.default,{offset:100,once:!0},o.default.createElement("img",{className:"inline","data-original":n,alt:t,title:t,src:n}))),o.default.createElement("p",null,o.default.createElement("strong",{className:"pexamName"},t),o.default.createElement("span",{className:"pexamCount"},s)))))}},{key:"render",value:function(){return o.default.createElement("section",{className:"predictorBanner"},o.default.createElement("div",{className:"_cntr"},o.default.createElement("div",{className:"heading3"},o.default.createElement("h2",{className:"tbSec2"},"Predict Colleges based on exams you have taken"