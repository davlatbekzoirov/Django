(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[7191],{38805:function(e,t,n){"use strict";n.d(t,{F:function(){return u},Y:function(){return s}});var r=n(52322),i=n(2784),o=(0,i.createContext)(null),s=function(e){var t=e.version,n=e.isKMP,s=e.isAnyBot,u=e.children,a=(0,i.useMemo)((function(){return{version:t,isKMP:n,isAnyBot:s}}),[t,n,s]);return(0,r.jsx)(o.Provider,{value:a,children:u})},u=function(){var e=(0,i.useContext)(o)||{},t=e.version,n=e.isKMP,r=e.isAnyBot;return(0,i.useMemo)((function(){if(!t)throw new Error("Unexpected device. Make sure that you add DeviceProvider to your route");return{isKMP:null!==n&&void 0!==n&&n,isMobile:"mobile"===t,isDesktop:"desktop"===t,device:t||"desktop",isAnyBot:r||!1}}),[t,n,r])}},34746:function(e,t,n){"use strict";n.d(t,{j_:function(){return d},Ys:function(){return f},hm:function(){return g}});var r=n(52322),i=n(2784),o=n(50930),s=[],u=function(e,t){switch(t.type){case"addFixedElement":return(0,o.Z)(e.filter((function(e){return e.name!==t.payload.name}))).concat([t.payload]);case"removeFixedElement":return e.filter((function(e){return e.name!==t.payload}));default:return e}},a={LEGO_CONVERSION_WITH_ANCHORS_MOBILE:{order:4,position:"bottom"},LEGO_PRICE_TABLE_CALL_TO_ACTION_BLOCK:{order:3,position:"bottom"},LEGO_VIDEO_FILES_FIXED_BLOCK:{order:2,position:"bottom"},LEGO_WIZARD_OPEN_BUTTON:{order:1,position:"bottom"}},c=function(){var e=(0,i.useReducer)(u,s),t=e[0],n=e[1],r=(0,i.useCallback)((function(e){n({type:"addFixedElement",payload:e})}),[]),o=(0,i.useCallback)((function(e){n({type:"removeFixedElement",payload:e})}),[]),c=(0,i.useCallback)((function(){return t.filter((function(e){return"top"===a[e.name].position})).reduce((function(e,t){return e+t.height}),0)}),[t]),l=(0,i.useCallback)((function(){return t.filter((function(e){return"bottom"===a[e.name].position})).reduce((function(e,t){return e+t.height}),0)}),[t]),d=(0,i.useCallback)((function(e){return t.filter((function(t){var n=a[e].position,r=a[t.name].position,i=a[e].order,o=a[t.name].order;return n===r&&("bottom"===n?i<o:i>o)})).reduce((function(e,t){return e+t.height}),0)}),[t]);return(0,i.useMemo)((function(){return{addFixedElement:r,removeFixedElement:o,getTopFixedElementsOffset:c,getBottomFixedElementsOffset:l,getSpecificFixedElementOffset:d,fixedElementsState:t,dispatchFixedElements:n}}),[r,o,c,l,d,t,n])},l=(0,i.createContext)({fixedElementsState:s,addFixedElement:function(){},removeFixedElement:function(){},getTopFixedElementsOffset:function(){return 0},getBottomFixedElementsOffset:function(){return 0},getSpecificFixedElementOffset:function(){return 0},dispatchFixedElements:function(){}}),d=function(e){var t=e.children,n=c();return(0,r.jsx)(l.Provider,{value:n,children:t})},g=function(){return(0,i.useContext)(l)};function f(e){var t=e.children,n=g(),i=n.getTopFixedElementsOffset,o=n.getBottomFixedElementsOffset,s=i(),u=o();return(0,r.jsx)("div",{style:{paddingTop:s?"".concat(s,"px"):void 0,paddingBottom:u?"".concat(u,"px"):void 0},children:t})}},60953:function(e,t,n){"use strict";n.d(t,{S:function(){return u},l:function(){return a}});var r=n(26297),i=n(52322),o=n(2784),s=(0,o.createContext)({}),u=function(e){var t=e.children,n=(0,r.Z)(e,["children"]);return(0,i.jsx)(s.Provider,{value:n,children:t})},a=function(){return(0,o.useContext)(s)}},43431:function(e,t,n){"use strict";n.d(t,{A:function(){return h}});var r=n(70865),i=n(96670),o=n(26297),s=n(52322),u=(n(2784),n(25237)),a=n.n(u),c=n(38805),l=n(60953),d=n(34746),g=a()((function(){return Promise.all([n.e(9846),n.e(4032),n.e(9097),n.e(6577),n.e(5944),n.e(2155)]).then(n.bind(n,23529))}),{loadableGenerated:{webpack:function(){return[23529]}}}),f=a()((function(){return Promise.all([n.e(9097),n.e(6577),n.e(5944),n.e(204)]).then(n.bind(n,90014))}),{loadableGenerated:{webpack:function(){return[90014]}}}),h=function(e){var t=e.version,n=e.showReviewReminder,u=e.isKMP,a=e.isAnyBot,h=e.pageType,v=(0,o.Z)(e,["version","showReviewReminder","isKMP","isAnyBot","pageType"]);return(0,s.jsx)(l.S,{showReviewReminder:n,pageType:h,children:(0,s.jsx)(d.j_,{children:(0,s.jsx)(c.Y,{version:t,isKMP:u,isAnyBot:a,children:"mobile"===t?(0,s.jsx)(f,(0,i.Z)((0,r.Z)({isMinimal:u},v),{"data-version":"mobile"})):(0,s.jsx)(g,(0,i.Z)((0,r.Z)({isMinimal:u},v),{"data-version":"desktop"}))})})})}},22903:function(e,t,n){"use strict";n.d(t,{K:function(){return l}});var r=n(52322),i=(n(2784),n(72779)),o=n.n(i),s=n(72063),u=n(74345),a=n(1288),c=n.n(a),l=function(e){var t=e.errorCode,n=e.errorText,i=e.className,a=e.isMobile,l=(0,u.h)(t)||{},d=l.errorTitle,g=l.errorExplanationSize,f=l.description,h="UNKNOWN_ERROR"===t&&n||f;return h||d?(0,r.jsxs)("div",{className:i,children:[(0,r.jsx)(s.xv,{size:"xl",bold:a,children:d}),h&&(0,r.jsx)(s.xv,{className:o()(c().description,a&&c().mobile),size:g,color:"muted",children:h})]}):null}},74345:function(e,t,n){"use strict";n.d(t,{h:function(){return l}});var r=n(70865),i=n(96670),o=n(52322),s=n(72063),u={size:"l",underlined:!0,target:"_blank",rel:"noopener"},a="\u0422\u0430\u043a\u043e\u0439 \u0443\u0441\u043b\u0443\u0433\u0438 \u043d\u0435\u0442 \u043d\u0430 \u041f\u0440\u043e\u0444\u0438",c={SPECIAL_GAS_LICENCE:{description:"\u0427\u0442\u043e\u0431\u044b \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0435\u0451, \u043d\u0443\u0436\u043d\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435. \u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u044c\u0441\u044f \u0432 \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0435\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e \u044d\u043a\u0441\u043f\u043b\u0443\u0430\u0442\u0430\u0446\u0438\u0438 \u0438 \u0440\u0435\u043c\u043e\u043d\u0442\u0443 \u0433\u0430\u0437\u043e\u0432\u043e\u0433\u043e \u0445\u043e\u0437\u044f\u0439\u0441\u0442\u0432\u0430.",errorTitle:a,imageType:"forbidden"},SPECIAL_CASHBOX_LICENCE:{description:"\u0427\u0442\u043e\u0431\u044b \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0435\u0451, \u043d\u0443\u0436\u043d\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435. \u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u044c\u0441\u044f \u0432 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044e, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043a\u0430\u0441\u0441\u043e\u0432\u044b\u0439 \u0430\u043f\u043f\u0430\u0440\u0430\u0442 \u0441\u0442\u043e\u0438\u0442 \u043d\u0430 \u0443\u0447\u0451\u0442\u0435.",errorTitle:a,imageType:"forbidden"},SPECIAL_SETUP_COUNTER_LICENCE:{description:"\u0427\u0442\u043e\u0431\u044b \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0435\u0451, \u043d\u0443\u0436\u043d\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435. \u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u044c\u0441\u044f \u0432 \u043e\u0433\u0440\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438, \u0443 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0435\u0441\u0442\u044c \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u044f \u043d\u0430 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443 \u0441\u0447\u0451\u0442\u0447\u0438\u043a\u043e\u0432.",errorTitle:a,imageType:"forbidden"},SPECIAL_REPAIR_COUNTER_LICENCE:{description:"\u0427\u0442\u043e\u0431\u044b \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0435\u0451, \u043d\u0443\u0436\u043d\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435. \u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u044c\u0441\u044f \u0432 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044e, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0443\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u043b\u0430 \u0441\u0447\u0451\u0442\u0447\u0438\u043a\u0438.",errorTitle:a,imageType:"forbidden"},DANGEROUS_GOODS:{description:"\u0427\u0442\u043e\u0431\u044b \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0435\u0451, \u043d\u0443\u0436\u043d\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435. \u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u044c\u0441\u044f \u0432 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438, \u0443 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0435\u0441\u0442\u044c \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u044f \u043d\u0430 \u043f\u0435\u0440\u0435\u0432\u043e\u0437\u043a\u0443 \u0442\u0430\u043a\u0438\u0445 \u0433\u0440\u0443\u0437\u043e\u0432.",errorTitle:a,imageType:"forbidden"},SPECIAL_LICENCE:{description:"\u0415\u0451 \u043c\u043e\u0433\u0443\u0442 \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0433\u0440\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438, \u0443 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0435\u0441\u0442\u044c \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435. \u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u044c\u0441\u044f \u043a \u043d\u0438\u043c.",errorTitle:a,imageType:"forbidden"},DEFAULT_SERVICE_FORBIDDEN_ERROR:{description:null,errorTitle:a,imageType:"forbidden"},PSYCHOLOGY:{description:"\u041c\u044b \u043d\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0430\u0435\u043c \u0441 \u043f\u0441\u0438\u0445\u0438\u0430\u0442\u0440\u0430\u043c\u0438, \u043f\u043e\u0442\u043e\u043c\u0443 \u0447\u0442\u043e \u043f\u043e\u043a\u0430 \u043d\u0435 \u0443\u043c\u0435\u0435\u043c \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c \u0438\u0445 \u043a\u0432\u0430\u043b\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044e. \u0423 \u043d\u0430\u0441 \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u043d\u0430\u0439\u0442\u0438 \u043f\u0441\u0438\u0445\u043e\u043b\u043e\u0433\u043e\u0432.\n     \u041e\u043d\u0438 \u043f\u043e\u043c\u043e\u0433\u0430\u044e\u0442 \u043c\u0435\u0442\u043e\u0434\u0430\u043c\u0438 \u043f\u0441\u0438\u0445\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u0438, \u043d\u043e \u043d\u0435 \u0432\u044b\u043f\u0438\u0441\u044b\u0432\u0430\u044e\u0442 \u0442\u0430\u0431\u043b\u0435\u0442\u043a\u0438.",errorTitle:a,imageType:"forbidden"},TRY_ANOTHER_SERVICE:{description:(0,o.jsxs)(o.Fragment,{children:["\u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043f\u043e\u0438\u0441\u043a\u0430\u0442\u044c \u043d\u0430 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0441\u0435\u0440\u0432\u0438\u0441\u0430\u0445. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043d\u0430"," ",(0,o.jsx)(s.rU,(0,i.Z)((0,r.Z)({to:"https://zoon.ru/"},u),{children:"Zoon"})),"."]}),errorTitle:a,imageType:"forbidden"},BABY_SITTERS:{description:(0,o.jsxs)(o.Fragment,{children:["\u0423 \u043d\u0430\u0441 \u0435\u0441\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043d\u044f\u043d\u0438, \u043a\u043e\u0442\u043e\u0440\u044b\u0435"," ",(0,o.jsx)(s.rU,(0,i.Z)((0,r.Z)({},u),{to:"/domashnii_personal/distancionnye-zanyatiya-dlya-detei/?seamless=1&tabName=ORDER&searchTerm=%D0%BD%D1%8F%D0%BD%D1%8F%20%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD#slideId=85465",children:"\u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442 \u043e\u043d\u043b\u0430\u0439\u043d"})),". \u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043f\u043e\u0438\u0441\u043a\u0430\u0442\u044c \u043d\u0430 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0441\u0435\u0440\u0432\u0438\u0441\u0430\u0445. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440,"," ",(0,o.jsx)(s.rU,(0,i.Z)((0,r.Z)({},u),{to:"https://kidsout.ru/",children:"Kidsout"})),"."]}),errorTitle:a,imageType:"forbidden"},TEXT_TOO_LONG:{errorTitle:"\u0421\u043b\u0438\u0448\u043a\u043e\u043c \u0434\u043b\u0438\u043d\u043d\u044b\u0439 \u0437\u0430\u043f\u0440\u043e\u0441",description:"\u0414\u0435\u0442\u0430\u043b\u0438 \u0437\u0430\u0434\u0430\u0447\u0438 \u043c\u043e\u0436\u043d\u043e \u0431\u0443\u0434\u0435\u0442 \u043e\u0431\u0441\u0443\u0434\u0438\u0442\u044c \u0441\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u043e\u043c.",imageType:"too-long"},UNKNOWN_ERROR:{errorTitle:"\u0423 \u043d\u0430\u0441 \u0447\u0442\u043e-\u0442\u043e \u0441\u043b\u043e\u043c\u0430\u043b\u043e\u0441\u044c.",description:"\u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u0435\u0449\u0451 \u0440\u0430\u0437 \u043f\u043e\u0437\u0436\u0435.",errorExplanationSize:"xl",imageType:"sys-error"}};function l(e){var t=c[e];return t?(0,i.Z)((0,r.Z)({},t),{errorExplanationSize:t.errorExplanationSize||"l"}):null}},37310:function(e,t,n){"use strict";n.d(t,{w:function(){return a}});var r=n(52322),i=(n(2784),n(72063)),o=n(40766),s=n(41693),u=n.n(s),a=function(e){var t,n,s=e.suggestion,a=s.value,c=s.highlighted,l=s.isWhiteOrderSuggestion,d=s.entities,g=e.isHighlighted;if(c){var f=c.replace(/\[/g,"<strong>").replace(/\]/g,"</strong>");n=(0,r.jsx)("span",{dangerouslySetInnerHTML:{__html:f}})}else n=a;return(0,r.jsxs)(i.aV.Item,{active:g,bodyClassName:u()["suggest-item"],trailing:l&&(0,r.jsx)(o.XC,{className:u()["additional-icon"]}),"data-shmid":"sage-suggest-item_".concat((null===(t=d[0])||void 0===t?void 0:t.kind)||"whiteOrder"),children:[(0,r.jsx)(i.aV.Item.MainText,{className:u()["suggest-text"],children:l&&"string"===typeof n?"\xab".concat(n,"...\xbb"):n}),l&&(0,r.jsx)(i.aV.Item.Caption,{children:"\u041e\u043f\u0438\u0441\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443 \u0441\u0432\u043e\u0438\u043c\u0438 \u0441\u043b\u043e\u0432\u0430\u043c\u0438"})]})}},56631:function(e,t,n){"use strict";n.d(t,{OU:function(){return s},Oh:function(){return o},Qf:function(){return a},lR:function(){return i},y4:function(){return r},y6:function(){return u}});var r=120,i=105,o="\u0423\u0441\u043b\u0443\u0433\u0430 \u0438\u043b\u0438 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442",s=20,u=10,a=[{title:"\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u043e\u043d\u043d\u043e"},{title:"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a \u043f\u043e \u0441\u043a\u0430\u0439\u043f\u0443"},{title:"\u041a\u043e\u043f\u0438\u0440\u0430\u0439\u0442\u0435\u0440"},{title:"\u0412\u0435\u0431-\u0434\u0438\u0437\u0430\u0439\u043d"},{title:"\u041c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433"},{title:"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0441\u0430\u0439\u0442\u043e\u0432"},{title:"\u041a\u0443\u0440\u044c\u0435\u0440",enabledCities:["msk","spb"]},{title:"\u041f\u0441\u0438\u0445\u043e\u043b\u043e\u0433 \u043e\u043d\u043b\u0430\u0439\u043d"},{title:"\u0421\u0430\u043d\u0442\u0435\u0445\u043d\u0438\u043a",enabledCities:["msk","spb"]},{title:"\u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u043d\u0430\u043b\u043e\u0433\u043e\u0432\u043e\u0439 \u0434\u0435\u043a\u043b\u0430\u0440\u0430\u0446\u0438\u0438"}]},66273:function(e,t,n){"use strict";n.d(t,{c:function(){return E},o:function(){return b}});var r=n(98788),i=n(70865),o=n(96670),s=n(66383),u=n(50853),a=n(2784),c=n(82066),l=n(41535),d=n(377),g=n(43713),f=n(20646),h="#prfrtkn:front:74f52f5d6122035b758809b41c73eb154214b8e1:412d5b020e3dffac7e129dca2d8d2ab95cb4960d\n\n      query Sage2($mode: SageMode!, $query: String!, $size: Int!, $conditions: [SageCondition!]!) {\n  sage2(mode: $mode, query: $query, size: $size, conditions: $conditions) {\n    hits {\n      text\n      highlighted\n      entities {\n        id\n        kind\n        source\n      }\n    }\n    tags {\n      ahead\n      text\n    }\n  }\n}\n      ",v=function(e,t){return(0,c.useQuery)(["Sage2",e],(0,f.yh)(h,e),t)};v.getKey=function(e){return["Sage2",e]};v.fetcher=function(e,t){return(0,f.yh)(h,e,t)};var A="#prfrtkn:front:94c0842ee0e4a72a6295fade4b4d50404b39f466:38e3b17dd90731d02cc414e779a6d9d7c2210412\n\n      query SageSubmitValidation($term: String!) {\n  sageSubmitValidation(term: $term) {\n    success\n    errors\n    errorCode\n  }\n}\n      ",m=function(e,t){return(0,c.useQuery)(["SageSubmitValidation",e],(0,f.yh)(A,e),t)};m.getKey=function(e){return["SageSubmitValidation",e]};m.fetcher=function(e,t){return(0,f.yh)(A,e,t)};var p=n(56631),_=v.getKey,y=v.fetcher,E=function(e,t){return function(n){var r=arguments.length>1&&void 0!==arguments[1]?arguments[1]:p.y6,s={mode:"suggest",query:e,size:p.y6,conditions:[{score:2,kind:[n],city:[t]}]};return{key:_(s),fetcher:y((0,o.Z)((0,i.Z)({},s),{size:r}))}}},b=function(e){var t=(0,l.R)(),n=(0,c.useQueryClient)(),i=(0,a.useCallback)(function(){var e=(0,r.Z)((function(e){var r,i,o,a,c,l,f,h,v,A,m,_,y,b;return(0,u.__generator)(this,(function(u){switch(u.label){case 0:return r=e.term,i=e.size,o=void 0===i?p.y6:i,a=e.reason,c=void 0===a?"term-changed":a,l=E(r,t),h=["service",!(f="get-popular-services"===c)&&r.length>=4?"profile":null].filter((function(e){return null!==e})),[4,Promise.all(h.map((function(e){var t=l(e,o),r=t.key,i=t.fetcher;return n.fetchQuery(r,i,{staleTime:36e5,cacheTime:36e5})})))];case 1:return(v=u.sent())&&!f&&(_=(0,s.Z)(v,2),y=_[0],b=_[1],d.SJ.registerEvent("service_search_suggests_shown",{search_query_text:r,search_query_length:r.length,search_suggests_count:(0,g.A1)((null===(A=y.sage2)||void 0===A?void 0:A.hits)||[],(null===b||void 0===b||null===(m=b.sage2)||void 0===m?void 0:m.hits)||[]),event_key:r})),[2,v]}}))}));return function(t){return e.apply(this,arguments)}}(),[t,n]),o=(0,a.useCallback)((function(e){e.term||(e.meta="raznoe");var t="/search/?".concat(new URLSearchParams(e).toString());window.open(t,"_self")}),[]),f=(0,a.useCallback)(function(){var t=(0,r.Z)((function(t){var r,i,s,a,c;return(0,u.__generator)(this,(function(u){switch(u.label){case 0:return r=m.getKey,i=m.fetcher,s={term:t},[4,n.fetchQuery(r(s),i(s))];case 1:return(null===(a=u.sent().sageSubmitValidation)||void 0===a?void 0:a.success)?o({term:t}):e({msg:(null===a||void 0===a||null===(c=a.errors)||void 0===c?void 0:c[0])||"\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u0430\u044f \u043e\u0448\u0438\u0431\u043a\u0430",code:(null===a||void 0===a?void 0:a.errorCode)||"UNKNOWN_ERROR"}),[2]}}))}));return function(e){return t.apply(this,arguments)}}(),[n,e,o]);return{fetchSageData:i,submit:f,selectSuggest:(0,a.useCallback)((function(e){var t={term:e.value},n=e.entities.find((function(e){return"service"===e.kind})),r=e.entities.find((function(e){return"project"===e.kind})),i=e.entities.filter((function(e){return"profile"===e.kind}));switch(!0){case!!n:t.service=null===n||void 0===n?void 0:n.id;break;case!!r:t.project=null===r||void 0===r?void 0:r.id;break;case 1===i.length:t.profile=i[0].id;break;case i.length>1:t.profile="multi"}o(t)}),[o])}}},9622:function(e,t,n){"use strict";n.d(t,{e:function(){return h}});var r=n(50930),i=n(2784),o=n(82066),s=n(66273),u=n(41535),a={keepPreviousData:!0,enabled:!1,refetchOnMount:!1},c=function(e,t){var n=(0,u.R)(),r=(0,s.c)(t,n)(e),i=r.key,c=r.fetcher;return(0,o.useQuery)(i,c,a)},l=function(e){var t=e.highlighted;return{value:e.text,highlighted:t,entities:e.entities,isWhiteOrderSuggestion:!1}};var d=function(e){var t,n,r,o,s,u,a=(0,i.useRef)({tags:[],hits:{services:[],profiles:[]}}),d=c("service",e),g=c("profile",e),f=(0,i.useMemo)((function(){var e,t;return((null===(e=d.data)||void 0===e||null===(t=e.sage2)||void 0===t?void 0:t.hits)||[]).map(l)}),[null===(t=d.data)||void 0===t||null===(n=t.sage2)||void 0===n?void 0:n.hits]),h=(0,i.useMemo)((function(){var e,t;return((null===(e=g.data)||void 0===e||null===(t=e.sage2)||void 0===t?void 0:t.hits)||[]).map(l)}),[null===(r=g.data)||void 0===r||null===(o=r.sage2)||void 0===o?void 0:o.hits]),v=null===(s=d.data)||void 0===s||null===(u=s.sage2)||void 0===u?void 0:u.tags,A=(0,i.useMemo)((function(){return function(e){var t=0,n=[],r=!0,i=!1,o=void 0;try{for(var s,u=e[Symbol.iterator]();!(r=(s=u.next()).done);r=!0){var a=s.value;if(n.push(a),(t+=a.ahead.length)>70)break}}catch(c){i=!0,o=c}finally{try{r||null==u.return||u.return()}finally{if(i)throw o}}return n}((v||[]).filter((function(e){return e.ahead})))}),[v]);return d.isFetching||g.isFetching||(a.current={tags:A,hits:{services:f,profiles:h}}),a.current},g=n(56631),f=function(e){var t=e.services,n=e.profiles;return(0,r.Z)(t).concat((0,r.Z)(n))},h=function(){var e=(0,i.useState)(""),t=e[0],n=e[1],r=(0,i.useState)(!1),o=r[0],s=r[1],u=(0,i.useState)(null),a=u[0],c=u[1],l=d(t),h=l.hits,v=h.services,A=h.profiles,m=v[0]||A[0];return{sage:l,highlightFirstSuggestion:!!(null===m||void 0===m?void 0:m.value)&&0===m.value.indexOf(t),sageTerm:t,isSuggestionSelected:o,submitError:a,setSageTerm:n,setSuggestionSelected:s,getComposedHits:f,setSubmitError:c,numbersWarning:g.lR<=t.length&&"".concat(t.length,"/").concat(g.y4),isInvalidTerm:t.length>g.y4}}},22877:function(e,t,n){"use strict";n.d(t,{e:function(){return c}});var r=n(2784),i=n(13255),o=n(377),s=n(43713),u=n(66273),a=n(56631),c=function(e){var t=e.sageTerm,n=e.getComposedHits,c=e.sage,l=c.hits,d=c.tags,g=e.submitError,f=e.setSuggestionSelected,h=e.setSageTerm,v=e.setSubmitError,A=(0,u.o)(v),m=A.submit,p=A.selectSuggest,_=A.fetchSageData,y=null===g||void 0===g?void 0:g.code,E=(0,i.DM)((function(e){var n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{isWhiteOrderSuggestion:!1};if(e&&e.preventDefault(),t){if(t.length>a.y4)return v({code:"TEXT_TOO_LONG"});var r=n.isWhiteOrderSuggestion;o.SJ.registerEvent(r?"service_search_showwhite_selected":"find_button_clicked",{search_query_text:t,search_query_length:t.length,search_suggests_count:(0,s.A1)(l.services,l.profiles)},{force:!0}),m(t)}}),[t,m]),b=(0,i.DM)((function(e,r){var i,u=r.suggestion;if(u.isWhiteOrderSuggestion)return E(e,{isWhiteOrderSuggestion:!0});var a=n(l).findIndex((function(e){return e.entities===u.entities&&e.highlighted===u.highlighted&&e.value===u.value}));o.SJ.registerEvent("service_search_suggest_selected",{search_query_text:t,search_query_length:t.length,search_suggest_text:u.value,search_suggest_position:a+1,search_suggest_type:"service"===(null===(i=u.entities[0])||void 0===i?void 0:i.kind)?"pservice":"prep",search_suggests_count:(0,s.A1)(l.services,l.profiles)},{force:!0}),p(u)}),[t,E,l]),S=(0,i.DM)((function(e){var t=e.value,n=e.reason;if(!(t.length>=a.y4)&&t)return"suggestion-selected"===n?f(!0):void _({term:t})}),[_,f]),x=(0,i.DM)((function(e){h(e.text),_({term:e.text}),o.SJ.registerEvent("tag_suggest_clicked",{search_query_text:t,search_query_length:t.length,search_tag_text:e.text,search_tags_count:d.length})}),[t,d,_]),C=(0,i.DM)((function(e,n){e.preventDefault();var r=n||{},i=r.method,u=r.newValue,a=void 0===u?"":u;"up"!==i&&"down"!==i&&(h(a),a||o.SJ.registerEvent("service_search_cleared",{search_query_text:t,search_query_length:t.length,search_suggests_count:(0,s.A1)(l.services,l.profiles)}),y&&v(null))}),[t,y,v]),T=r.useCallback((function(e){h(e),m(e)}),[h,m]),I=r.useCallback((function(){o.SJ.registerEvent("page_service_search_shown"),o.wT.registerEvent("page_service_search_shown")}),[]),O=r.useCallback((function(e){e?y&&v(null):I()}),[y,v,I]),M=r.useCallback((function(){_({term:"",reason:"get-popular-services",size:a.OU})}),[_]);return{handleSubmit:E,handleChange:C,handleSuggestionSelected:b,handleSuggestionsFetchRequested:S,handleTagSelect:x,handleFocus:I,handleFocusMobile:O,handleClickHint:T,handleFetchPopularServices:M}}},43713:function(e,t,n){"use strict";n.d(t,{A1:function(){return l},jn:function(){return c},U7:function(){return d}});var r=n(45393),i=n.n(r),o=n(74345),s={src:"/_next/static/media/ForbiddenServices.a55b12af.png",height:121,width:121,blurDataURL:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAMAAADz0U65AAAAElBMVEVMaXEyMjIyMjIyMjIyMjIyMjK6RmCnAAAABnRSTlMAKEUVN2oUUIKyAAAACXBIWXMAAAsTAAALEwEAmpwYAAAALElEQVQImTWJQQ4AIAzCCmz//7IRY8OBAsAMRYla3Fz+hd/gSDGoOoKstOEACIYAR4BLno8AAAAASUVORK5CYII=",blurWidth:8,blurHeight:8},u={src:"/_next/static/media/TooLong.d6d82814.png",height:121,width:121,blurDataURL:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAMAAADz0U65AAAAG1BMVEUyMjIyMjJMaXEyMjIyMjIyMjIyMjIyMjIyMjKThOqHAAAACXRSTlNcQAApTXMNFzFrUDulAAAACXBIWXMAAAsTAAALEwEAmpwYAAAANElEQVQImR3GQQ7AQAwCsQFCsv9/caX6ZDZ5sQ2d9myuOpXFs34lf8IEa0QV7IUbYXtH6AMfzwDL83CEpwAAAABJRU5ErkJggg==",blurWidth:8,blurHeight:8},a={src:"/_next/static/media/SearchError.30ee5c87.png",height:121,width:121,blurDataURL:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAMAAADz0U65AAAAGFBMVEUyMjJMaXEyMjIyMjIyMjIyMjIyMjIyMjIm9TC5AAAACHRSTlNHABAZWiwjjtvX5zkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAwSURBVAiZFcrBEcAwAMIwG0iy/8a96i30QhShZ5VDTCckb1Joh4Tsn4h3sAW1tecDEcoAgpPIDzkAAAAASUVORK5CYII=",blurWidth:8,blurHeight:8};function c(e,t){var n=e.filter((function(e){return!e.enabledCities||e.enabledCities.includes(t)})).map((function(e){return e.title}));return i()(n,3)}var l=function(){for(var e=arguments.length,t=new Array(e),n=0;n<e;n++)t[n]=arguments[n];return t.reduce((function(e,t){return e+((null===t||void 0===t?void 0:t.length)||0)}),0)},d=function(e){if(!e)return null;var t=((0,o.h)(e)||{}).imageType;switch(void 0===t?null:t){case"too-long":return u;case"forbidden":return s;case"sys-error":return a;default:return null}}},1288:function(e){e.exports={description:"ErrorsAndForbiddenServices_description__3vUyR",mobile:"ErrorsAndForbiddenServices_mobile__n_6ll"}},41693:function(e){e.exports={"suggest-item":"SuggestionItem_suggest-item__hQ9ds","additional-icon":"SuggestionItem_additional-icon__7zDLf","suggest-text":"SuggestionItem_suggest-text___kY9G"}}}]);