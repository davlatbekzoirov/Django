"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[4032],{4032:function(e,n,t){t.d(n,{nx:function(){return r},J8:function(){return m},kC:function(){return E},F3:function(){return b},SZ:function(){return O},Jp:function(){return u},nl:function(){return x},Ho:function(){return y},CE:function(){return L},VO:function(){return k},rS:function(){return V},O8:function(){return d},Qj:function(){return v},Tx:function(){return G},O$:function(){return p},L7:function(){return A},Dr:function(){return N},sq:function(){return j},Kr:function(){return R},GS:function(){return h},DG:function(){return F},Gw:function(){return S},zl:function(){return T},F8:function(){return M},ZG:function(){return _}});var r={};t.r(r),t.d(r,{K5:function(){return i},_Q:function(){return o},oh:function(){return c},SV:function(){return l},L_:function(){return a}});var u=t(86814),i=13,o=27,a=32,c=37,l=39,s=([{id:"jan",shortName:"\u042f\u043d\u0432",fullName:"\u042f\u043d\u0432\u0430\u0440\u044c"},{id:"feb",shortName:"\u0424\u0435\u0432",fullName:"\u0424\u0435\u0432\u0440\u0430\u043b\u044c"},{id:"mar",shortName:"\u041c\u0430\u0440",fullName:"\u041c\u0430\u0440\u0442"},{id:"apr",shortName:"\u0410\u043f\u0440",fullName:"\u0410\u043f\u0440\u0435\u043b\u044c"},{id:"may",shortName:"\u041c\u0430\u0439",fullName:"\u041c\u0430\u0439"},{id:"jun",shortName:"\u0418\u044e\u043d",fullName:"\u0418\u044e\u043d\u044c"},{id:"jul",shortName:"\u0418\u044e\u043b",fullName:"\u0418\u044e\u043b\u044c"},{id:"aug",shortName:"\u0410\u0432\u0433",fullName:"\u0410\u0432\u0433\u0443\u0441\u0442"},{id:"sep",shortName:"\u0421\u0435\u043d",fullName:"\u0421\u0435\u043d\u0442\u044f\u0431\u0440\u044c"},{id:"oct",shortName:"\u041e\u043a\u0442",fullName:"\u041e\u043a\u0442\u044f\u0431\u0440\u044c"},{id:"nov",shortName:"\u041d\u043e\u044f",fullName:"\u041d\u043e\u044f\u0431\u0440\u044c"},{id:"dec",shortName:"\u0414\u0435\u043a",fullName:"\u0414\u0435\u043a\u0430\u0431\u0440\u044c"}].map((e=>e.fullName)),[{id:"mo",shortName:"\u041f\u043d",fullName:"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a"},{id:"tu",shortName:"\u0412\u0442",fullName:"\u0412\u0442\u043e\u0440\u043d\u0438\u043a"},{id:"we",shortName:"\u0421\u0440",fullName:"\u0421\u0440\u0435\u0434\u0430"},{id:"th",shortName:"\u0427\u0442",fullName:"\u0427\u0435\u0442\u0432\u0435\u0440\u0433"},{id:"fr",shortName:"\u041f\u0442",fullName:"\u041f\u044f\u0442\u043d\u0438\u0446\u0430"},{id:"sa",shortName:"\u0421\u0431",fullName:"\u0421\u0443\u0431\u0431\u043e\u0442\u0430"},{id:"su",shortName:"\u0412\u0441",fullName:"\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435"}]),f=(s.reduce(((e,n,t)=>Object.assign(Object.assign({},e),{},{[t+1]:n.shortName})),{}),s.length,t(2784)),d=(e,n)=>{var t=(0,f.useCallback)((t=>{var r;!e.current||null!==(r=e.current)&&void 0!==r&&r.contains(t.target)||n(t)}),[n,e]);(0,f.useEffect)((()=>(document.addEventListener("click",t),()=>document.removeEventListener("click",t))),[t])};function v(...e){var n=(0,f.useRef)(),t=(0,f.useCallback)((function(t){[].concat(e,[n]).forEach((e=>{"function"===typeof e?e(t):e&&(e.current=t)}))}),e);return[n,t]}function m(){return!("undefined"===typeof window||!window.document||!window.document.createElement)}var h=(e,n=!1)=>{var[t,r]=(0,f.useState)(m()?()=>window.matchMedia(e).matches:n);return(0,f.useEffect)((()=>{var n=!0,t=window.matchMedia(e),u=()=>{n&&r(!!t.matches)};return t.addListener(u),r(t.matches),()=>{n=!1,t.removeListener(u)}}),[e]),t},w={mobile:"(min-width: 320px) and (max-width: 767px)",tablet:"(min-width: 768px) and (max-width: 1023px)",tabletHorizontal:"(min-width: 1024px) and (max-width: 1280px)",desktop:"(min-width: 1280px)"};function p(e,n){return h(w[e],n)}function N(e=!1,n){var[t,r]=(0,f.useState)(e);return(0,f.useEffect)((()=>{r(e)}),[e]),[t,{onFocus:(0,f.useCallback)((e=>{n.onFocus&&n.onFocus(e),r(!0)}),[n]),onBlur:(0,f.useCallback)((e=>{n.onBlur&&n.onBlur(e),e.target.value||r(!1)}),[n])}]}function g(e,n){var t=(0,f.useRef)(e);(0,f.useEffect)((()=>{t.current=e}),n);var r=(0,f.useCallback)(((...e)=>{var n;return null===(n=t.current)||void 0===n?void 0:n.call.apply(n,[t].concat(e))}),[]);return e?r:null}function _(e,n){var t=(0,f.useRef)(n),r=t.current;r===n||r.length===n.length&&!r.some(((e,t)=>!Object.is(e,n[t])))||e(),t.current=n}var b=(e,n,t)=>{var r=[],u=e.slice(),i=t?u.length%n:0;for(i&&r.push(u.splice(0,i));u.length>0;)r.push(u.splice(0,n));return r};function E(e){return e.slice(0,1).toUpperCase()+e.slice(1)}var x=(e,n)=>Math.abs(e+n)%e;function k(e){return e?Object.entries(null!==e&&void 0!==e?e:{}).map((([e,n])=>{return`${t=e,t.replace(/([A-Z])/g,"-$1").toLowerCase()}:${n}`;var t})).join(";"):""}function C(e,n=800,t=-1){if(!(n<=0)){var r=(e=>{var n=document.body.scrollHeight-window.innerHeight;return e>n?n:e})(e),u=window.pageYOffset,i=function(e,n,t,r){return t*(e/=r)*e+n}(++t,u,r-u,n),o=()=>{clearTimeout(a),window.removeEventListener("mousewheel",o)},a=setTimeout((()=>{if(window.scrollTo(0,i),window.pageYOffset===e)return o();C(e,n-10,t),o()}),10);window.addEventListener("mousewheel",o)}}function y(e,n,t,r){var u=Math.abs(e);return(u%=100)>=5&&u<=20?r:1===(u%=10)?n:u>=2&&u<=4?t:r}function L(e){return e?(e=e.toString()).length>4?e.replace(/\B(?=(\d{3})+(?!\d))/g,"\u202f"):e.toString():""}var O=(e,n)=>n?f.Children.toArray(e).find((e=>(e=>{if(f.isValidElement(e)){var{type:n}=e;return"string"===typeof n?null:n}return null})(e)===n)):null,S=m()?f.useLayoutEffect:f.useEffect;function j(e,n){var t=(0,f.useCallback)((()=>{setTimeout((()=>{var{top:n}=e.current.getBoundingClientRect()||{};n>window.innerHeight/2&&C(window.pageYOffset+n-window.innerHeight/2)}),500)}),[e]);S((()=>{var{current:r}=e;if(n&&r)return r.addEventListener("focus",t),()=>r.removeEventListener("focus",t)}),[e,t,n])}function R(e,n){var t=g((({key:t,keyCode:r})=>{var u=isNaN(+t)?r:t;String(u)===String(e)&&n()}));(0,f.useEffect)((()=>(window.addEventListener("keydown",t),()=>{window.removeEventListener("keydown",t)})),[t])}var H=e=>{e.selectionStart=e.selectionEnd=e.value.length};function F({ref:e,mode:n="onMount",deps:t}){var r=(0,f.useRef)(n);(0,f.useEffect)((()=>{if("onFocus"===r.current){var n=null===e||void 0===e?void 0:e.current;if(!n)return;var t=()=>{H(n)};return n.addEventListener("focus",t),()=>{n.removeEventListener("focus",t)}}}),t),(0,f.useEffect)((()=>{var n=null===e||void 0===e?void 0:e.current;"onMount"===r.current&&n&&H(n)}),[r,e])}function T(e,n,t=200,r={leading:!0,trailing:!0}){var u=(0,f.useRef)(),i=(0,f.useRef)(void 0),o=(0,f.useRef)(!1);return(0,f.useEffect)((()=>function(){clearTimeout(u.current)}),[]),(0,f.useCallback)(((...n)=>{if(u.current)i.current=()=>e.apply(void 0,n),o.current=!0;else{r.leading?e.apply(void 0,n):(i.current=()=>e.apply(void 0,n),o.current=!0);var a=()=>{r.trailing&&o.current?(o.current=!1,i.current(),u.current=setTimeout(a,t)):u.current=void 0};u.current=setTimeout(a,t)}}),n)}var z=t(83096);function A(e,n=!0){f.useEffect((()=>{var t="current"in e?e.current:e;return(n?z.Qp:z.tG)(t),()=>(0,z.tG)(t)}),[e,n])}function G(e){var{value:n,defaultValue:t,onChange:r,shouldUpdate:u=((e,n)=>e!==n)}=e,i=g(r),o=g(u),[a,c]=f.useState(t),l=void 0!==n,s=l?n:a,d=f.useCallback((e=>{var n=function(e,...n){return"function"===typeof e?e.apply(void 0,n):e}(e,s);o(s,n)&&(l||c(n),null===i||void 0===i||i(n))}),[l,i,s,o]);return[s,d]}var I=()=>{var[e,n]=(0,f.useState)();return S((()=>{"IntersectionObserver"in window?n((()=>window.IntersectionObserver)):t.e(8360).then(t.t.bind(t,18360,23)).then((()=>n((()=>window.IntersectionObserver))))}),[]),e},M=({options:e={threshold:1},ref:n,onVisibilityChanged:t,visible:r})=>{var u=(0,f.useRef)(),i=n||u,o=I(),[a,c]=G({value:r,onChange:e=>t(e),defaultValue:!1}),l=g((([n])=>{c(n.intersectionRatio>=e.threshold)}),[c]),s=(0,f.useRef)(e),d=(0,f.useMemo)((()=>o?new o(l,s.current):null),[o,l]);return(0,f.useEffect)((()=>(null===d||void 0===d||d.observe(i.current),()=>null===d||void 0===d?void 0:d.disconnect())),[d,i]),{visible:a,onVisibilityChanged:t,ref:i,disconnect:()=>d.disconnect()}},V={common:{bold:"ui_RF7aD",regular:"ui_3nAGW","size-xs":"ui_38jwe","size-s":"ui_237c5","size-m":"ui_1hoX9","size-l":"ui_3Y-uv","size-xl":"ui_3j-OD","size-xxl":"ui_3owa1","radius-xs":"ui_22N1O","radius-s":"ui_iIKP2","radius-m":"ui_3IT2O","radius-l":"ui_2IFIt","radius-xl":"ui_1K_V9","radius-ml":"ui_saSa6","radius-xxl":"ui_3uEcF","color-brand":"ui_1xgvX","color-primary":"ui_p8KJN","color-secondary":"ui_gBDdc","color-light":"ui_HkEHH","color-danger":"ui_3a6SQ","color-success":"ui_2oEgH","color-warning":"ui_3GQtd"},variables:{},transitions:{slide:{enter:"ui_3hIjW",enterActive:"ui_2uO3U",exit:"ui_2w-2L",exitActive:"ui_duCsW"},fade:{enter:"ui_2YA4W",enterActive:"ui_2HtDU",exit:"ui_EnkgQ",exitActive:"ui_2TnM-"},skeleton:"ui_2SFCo"}}}}]);