h",this.ga);a.D&&!this.H||H(b,"scsm_shash",this.ha);return b};
w.se=function(a){switch(a){case "scsm_smodel":return this.O;case "scsm_ss":return this.la;case "scsm_stag":return this.V;case "scsm_stype":return this.aa;case "scsm_cshash":return this.ga;case "scsm_shash":return this.ha;default:throw G("sb`"+F(a)).D;}};w.$d=function(a){switch(a){case "scsm_smodel":return this.J;case "scsm_ss":return!0;case "scsm_stag":return this.R;case "scsm_stype":return this.W;case "scsm_cshash":return this.D;case "scsm_shash":return this.H}return!1};
w.ke=function(a,b){return a instanceof VKa?!b.D||this.J==a.J&&this.R==a.R&&this.W==a.W&&this.D==a.D&&this.H==a.H?this.O==a.O&&this.V==a.V&&this.aa==a.aa&&xo(this.la,a.la,b)&&Vf(this.ga,a.ga)&&Vf(this.ha,a.ha):!1:!1};w.gi=function(){return WKa};w.clone=function(){var a=new VKa({});this.copyTo(a);return a};w.De=function(a){a.O=this.O;a.J=this.J;a.la=this.la.clone();a.V=this.V;a.R=this.R;a.aa=this.aa;a.W=this.W;a.ga=this.ga;a.D=this.D;a.ha=this.ha;a.H=this.H};function XKa(a){YKa();No.call(this,"spellcheck",(UKa(),TKa));this.R=this.O=!1;this.H=this.D=null;this.J=new ir(new Qu);this.V=new ir(cq(ZKa));a&&this.Nd(a)}function ZKa(a){return new VKa(a)}var $Ka=["sc_sugg","sc_sm"];function aLa(){return new XKa(null)}function bLa(){return UKa(),TKa}var cLa;x(XKa,No);w=XKa.prototype;
w.ve=function(a,b){var c=!!b&&b.D;if("sc_ow"in a&&(!c||this.O)){var d=a.sc_ow;this.O=!0;this.D=d}"sc_sl"in a&&(!c||this.R)&&(c=a.sc_sl,this.R=!0,this.H=c);"sc_sugg"in a&&this.J.update(a.sc_sugg,b);"sc_sm"in a&&this.V.update(a.sc_sm,b)};w.Ae=function(a){var b={};a.D&&!this.O||H(b,"sc_ow",this.D);a.D&&!this.R||H(b,"sc_sl",this.H);var c=this.J.Va(a);Gn(a,c)&&H(b,"sc_sugg",c);c=this.V.Va(a);Gn(a,c)&&H(b,"sc_sm",c);return b};
w.se=function(a){switch(a){case "sc_ow":return this.D;case "sc_sl":return this.H;case "sc_sugg":return this.J;case "sc_sm":return this.V;default:throw G("sb`"+F(a)).D;}};w.$d=function(a){switch(a){case "sc_ow":return this.O;case "sc_sl":return this.R;case "sc_sugg":return!0;case "sc_sm":return!0}return!1};w.ke=function(a,b){return a instanceof XKa?!b.D||this.O==a.O&&this.R==a.R?Vf(this.D,a.D)&&Vf(this.H,a.H)&&xo(this.J,a.J,b)&&xo(this.V,a.V,b):!1:!1};w.gi=function(){return $Ka};
w.clone=function(){var a=new XKa(null);this.copyTo(a);return a};w.De=function(a){a.D=this.D;a.O=this.O;a.H=this.H;a.R=this.R;a.J=this.J.clone();a.V=this.V.clone()};function YKa(){YKa=h();Oo();cLa=To("spellcheck",aLa,bLa)};var dLa,eLa;function fLa(){fLa=h();dLa=aq($p(Zp(Zxa((Owa(),Mwa)),"vcs_c"),rg([(Tn(),Qn),Rn,Sn],On,Un,1)));eLa=fo([dLa])};function gLa(a){hLa();Ru.call(this,"vcs_c","voice_corrections",(fLa(),eLa),a)}function iLa(){return new gLa(null)}function jLa(){return fLa(),eLa}var kLa;x(gLa,Ru);gLa.prototype.clone=function(){var a=new gLa(null);this.copyTo(a);return a};function hLa(){hLa=h();Oo();kLa=To("voice_corrections",iLa,jLa)};var lLa,mLa;function nLa(){nLa=h();lLa=vp(up(rp(qp(op(),"vdss_p")),rg([(Tn(),Qn),Rn,Sn],On,Un,1)));mLa=fo([lLa])};function oLa(a){pLa();No.call(this,"voice_dotted_span",(nLa(),mLa));this.D=!1;a&&this.Nd(a)}function qLa(){return new oLa(null)}function rLa(){return nLa(),mLa}var sLa;x(oLa,No);w=oLa.prototype;w.ve=function(a,b){b=!!b&&b.D;"vdss_p"in a&&(!b||this.D)&&(a=a.vdss_p,this.D=!0,this.H=a)};w.Ae=function(a){var b={};a.D&&!this.D||H(b,"vdss_p",this.H);return b};w.se=function(a){switch(a){case "vdss_p":return this.H}throw G("sb`"+F(a)).D;};w.$d=function(a){switch(a){case "vdss_p":return this.D}return!1};
w.ke=function(a,b){return a instanceof oLa?b.D&&this.D!=a.D?!1:Vf(this.H,a.H):!1};w.clone=function(){var a=new oLa(null);this.copyTo(a);return a};w.De=function(a){a.H=this.H;a.D=this.D};function pLa(){pLa=h();Oo();sLa=To("voice_dotted_span",qLa,rLa)};var tLa=[(cKa(),gKa),(mKa(),pKa),(vKa(),yKa),(DKa(),GKa),(Xr(),UCa),(Au(),mIa),(nr(),UBa),(YKa(),cLa),(Uq(),OAa),(RJa(),UJa)];Q(P(),"sketchy-evt")&&(tLa.push((hLa(),kLa)),tLa.push((pLa(),sLa)));var Uu=FCa(tLa);function uLa(a,b,c){MJa.call(this,a,b);this.F=c}x(uLa,MJa);uLa.prototype.D=function(a){if(void 0!==this.key){a[this.key]=this.value;var b=eo(Uu.Mf(this.F),String(this.key));b&&(a[b]=!1)}};function vLa(a,b){MJa.call(this,a,b)}x(vLa,MJa);vLa.prototype.D=function(a){void 0!==this.key&&(a[this.key]=this.value)};var wLa=null;function Vu(){wLa||(wLa=new Nna);return wLa};function Wu(a){this.D={};if(a)for(var b in a)this.set(b,a[b])}x(Wu,E);Wu.prototype.get=function(a){if(!(a in this.D))throw G("je`"+F(a)).D;return this.D[a]};Wu.prototype.set=function(a,b){H(this.D,a,b)};function xLa(){this.J=new Wu;this.H=new Wu}xLa.prototype.D=function(a,b,c){return this.J.get(a).D(a,b,c)};xLa.prototype.F=function(a,b,c){return this.H.get(a).F(a,b,c)};function Xu(a,b){yLa.H.set(a,b)}function Yu(a,b){yLa.J.set(a,b)};function zLa(a,b,c,d){0==(0==a?0:a-1)&&0==b?(c=Jb(c),Kb(c,{kixStartIndex:a,kixEndIndex:b,type:d}),Ij(Vu(),Error("ke"),c)):0==a&&(c=Jb(c),Kb(c,{kixStartIndex:a,kixEndIndex:b,type:d}),Vu().log(Error("le"),c))}function ALa(a){var b={},c;for(c in a){var d=Number(c),e=Zu[d];if(void 0!==e&&("voice_corrections"!=e&&"voice_dotted_span"!=e||Q(P(),"sketchy-evt"))){var f=b[e];f?f[d]=a[d]:(f={},f[d]=a[d],b[e]=f)}}return b}
function BLa(a,b){b=b||{};a=a||[];var c=tba(b);if(c)return Zu[c];if(c=a[0])return Zu[c];var d,e;for(e in b)b=Zu[Number(e)],void 0===d&&(d=b);for(e=0;e<a.length;e++)b=Zu[a[e]],void 0===d&&(d=b);return d}
function CLa(a,b,c,d,e){for(var f=DLa.get(a),g={},k=!1,l=[],m=0;m<b.length;m++){var n=b[m];if(n in ELa)l.push(n),k=!0;else{n=$u.get(String(n));var q=eo(Uu.Mf(f),n);q?g[q]=!0:g[n]="sc_sugg"==n?jr([]):"sc_sm"==n?jr([]):n in FLa?jr([]):null}}b={};for(var t in c)f=Number(t),f in GLa||(f in ELa?(b[f]=c[f],k=!0):(m=c[f],$u.get(String(f))in FLa&&(m=jr(m)),e.D(a,f,m).D(g)));if(d)for(var u in d)c=Number(u),t=pBa(Pxa(d[c])),e.D(a,c,t).D(g);k&&(l=HLa(l),b=ILa(b),g.ls_ts=CLa("text",l,b,null,e));return g}
function JLa(a,b){b=Uu.Mf(b);var c=[],d;for(d in a){var e=a[d];if("ls_ts"==d)null===e&&(e=Xq().Va()),ab(c,KLa(JLa(e,"text")));else if(!Pa(LLa,d)){var f=bo(b,d);f&&e?(e=co(b,d),e=ct($u).get(e),c.push(Number(e))):f||null!=e||c.push(Number(ct($u).get(d)))}}return c}
function MLa(a,b){var c={},d=ct(NLa);b=Uu.Mf(b);var e={},f=Q(P(),"docs-text-etsrds"),g;for(g in a){var k=a[g];"ts_rtd"==g?f&&(c[g]=k):d.get(g)||"ls_ts"==g?c[g]=k:bo(b,g)&&d.get(co(b,g))&&(c[g]=k,e[g]=k)}for(var l in e)a=e[l],d=co(b,l),a&&delete c[d];return c}function OLa(a,b,c){var d={},e=!0,f;for(f in FLa)f in a&&(c.F(b,f,a[f].cv).D(d),e=!1);a={};for(var g in d)a[g]=Sxa(d[g]);return e?null:a}
function PLa(a,b,c){var d=Uu.Mf(b),e={},f;for(f in a){var g=a[f];if("ls_ts"==f)wa(g)&&Kb(e,QLa(PLa(g,"text",c)));else if(!(bo(d,f)||f in FLa)){var k=eo(d,f);a[k]||null==g||c.F(b,f,g).D(e)}}return e}function QLa(a){var b={},c;for(c in a){var d=RLa.get(c);void 0!==d&&(b[d]=a[c])}return b}function ILa(a){var b={},c;for(c in a){var d=ct(RLa).get(c);void 0!==d&&(b[Number(d)]=a[c])}return b}function KLa(a){for(var b=[],c=0;c<a.length;c++){var d=RLa.get(a[c]);void 0!==d&&b.push(d)}return b}
function HLa(a){for(var b=[],c=0;c<a.length;c++){var d=ct(RLa).get(a[c]);void 0!==d&&b.push(Number(d))}return b}
var Zu={0:"text",49:"comment",9:"text",1:"text",2:"text",10:"text",20:"text",3:"text",4:"text",5:"text",6:"text",56:"text",7:"text",50:"text",11:"paragraph",62:"paragraph",12:"paragraph",13:"paragraph",14:"paragraph",30:"paragraph",15:"paragraph",16:"paragraph",39:"paragraph",28:"paragraph",42:"paragraph",43:"paragraph",44:"paragraph",8:"link",31:"list",32:"list",19:"list",21:"list",22:"list",23:"list",24:"list",33:"list",25:"list",26:"list",57:"list",18:"list",27:"list",17:"list",36:"list",37:"list",
34:"spellcheck",35:"spellcheck",61:"spellcheck",55:"spellcheck",38:"ignore_word",40:"date_time",41:"date_time",53:"voice_corrections",52:"voice_dotted_span",58:"composing_region",59:"composing_decoration",60:"composing_decoration"},SLa={0:"ts_bd",1:"ts_it",2:"ts_un",10:"ts_sc",20:"ts_st",3:"ts_bgc2",4:"ts_fgc2",5:"ts_ff",6:"ts_fs",56:"ts_tw",7:"ts_va",50:"ts_rtd",11:"ps_ls",62:"ps_lslm",12:"ps_al",30:"ps_ltr",28:"ps_ifl",13:"ps_il",14:"ps_ir",15:"ps_sb",16:"ps_sa",39:"ps_sm",42:"ps_awao",43:"ps_klt",
44:"ps_kwn",8:"lnks_link",18:"ls_nest",27:"ls_id",34:"sc_ow",35:"sc_sugg",61:"sc_sm",55:"sc_sl",38:"iwos_i",40:"dts_f",41:"dts_l",49:"cs_cids",53:"vcs_c",52:"vdss_p",58:"cr_c",59:"cd_u",60:"cd_bgc"},$u=new Pu(SLa),NLa=new bt(SLa),RLa=new bt({7:31,0:23,3:32,4:19,5:21,6:22,1:24,10:33,20:26,56:57,2:25}),TLa={text:"text",paragraph:"paragraph",link:"link",list:"list",spellcheck:"spellcheck",ignore_word:"ignore_word",date_time:"date_time",comment:"comment",voice_corrections:"voice_corrections",voice_dotted_span:"voice_dotted_span",
composing_region:"composing_region",composing_decoration:"composing_decoration"},DLa=new Pu(TLa),ULa=new bt(TLa),ELa={31:!0,32:!0,23:!0,19:!0,21:!0,22:!0,24:!0,33:!0,26:!0,57:!0,25:!0},FLa={cs_cids:!0},GLa={9:!0},LLa="ps_bbtw_i ps_bb_i ps_bl_i ps_br_i ps_bt_i ps_sd_i".split(" ");function av(){}av.prototype.F=function(a,b,c){return new vLa(Number(ct($u).get(b)),c)};av.prototype.D=function(a,b,c){var d=$u.get(String(b));switch(Nm[b]){case 1:c=!!c}a=DLa.get(a);return new uLa(d,c,a)};function VLa(a){if(null==a)return new dq({hclr_color:null});switch(a.getType()){case 1:return 0==a.getOpacity()?new dq({hclr_color:null}):new dq({hclr_color:a.bd()});case 2:return new eza({sclr_index:a.getIndex()});default:throw Error("vc`"+a.getType());}}function WLa(a){var b=a.clr_type;switch(b){case 0:return(a=a.hclr_color)?new vs(a,1):mFa(3);case 1:return new ws(a.sclr_index);default:throw Error("me`"+b);}};function XLa(){}x(XLa,av);XLa.prototype.F=function(a,b,c){if("ts_va"==b)c=ct(YLa).get(c),c=Number(c);else if("ts_fgc2"==b||"ts_bgc2"==b)c=WLa(c);return av.prototype.F.call(this,a,b,c)};XLa.prototype.D=function(a,b,c){if(7==b)c=YLa.get(String(c));else if(3==b||4==b)c=VLa(c).Va();else if(9==b)return new uLa;return av.prototype.D.call(this,a,b,c)};var YLa=new Pu({2:"sub",1:"sup",0:"nor"});function ZLa(){}x(ZLa,av);function $La(){}x($La,av);$La.prototype.F=function(a,b,c){"cd_bgc"==b&&(c=WLa(c));return av.prototype.F.call(this,a,b,c)};$La.prototype.D=function(a,b,c){60==b&&(c=VLa(c).Va());return av.prototype.D.call(this,a,b,c)};function aMa(){}x(aMa,av);function bMa(){}x(bMa,av);function cMa(){}x(cMa,av);function dMa(){}x(dMa,av);dMa.prototype.F=function(a,b,c){"lnks_link"==b&&(c=c.ulnk_url);return av.prototype.F.call(this,a,b,c)};dMa.prototype.D=function(a,b,c){8==b&&(c={lnk_type:0,ulnk_url:c});return av.prototype.D.call(this,a,b,c)};function eMa(){}x(eMa,av);eMa.prototype.D=function(a,b,c){switch(b){case 29:case 17:return new uLa}return av.prototype.D.call(this,a,b,c)};function fMa(){}x(fMa,av);fMa.prototype.F=function(a,b,c){"ps_al"==b?(c=ct(gMa).get(String(c)),c=Number(c)):"ps_ls"==b?c*=100:"ps_ltr"==b&&(c=Number(!c));return av.prototype.F.call(this,a,b,c)};fMa.prototype.D=function(a,b,c){12==b?0==c?c=0:(c=gMa.get(String(c)),c=Number(c)):11==b?c/=100:30==b&&(c=!c);return av.prototype.D.call(this,a,b,c)};var gMa=new Pu({1:0,2:1,3:2,4:3});function hMa(){}x(hMa,av);hMa.prototype.D=function(a,b,c){35==b&&(c=jr(c.concat()));if(61==b){for(var d=[],e=0;e<c.length;e++){var f=c[e];if(0<f.length){var g={};g.scsm_ss=jr(f[0].concat());d.push(g)}}c=jr(d)}return av.prototype.D.call(this,a,b,c)};function iMa(){}x(iMa,av);function jMa(){}x(jMa,av);function bv(){if(yLa)return yLa;yLa=new xLa;var a=new XLa;Xu("text",a);Yu("text",a);a=new fMa;Xu("paragraph",a);Yu("paragraph",a);a=new dMa;Xu("link",a);Yu("link",a);a=new eMa;Xu("list",a);Yu("list",a);a=new hMa;Xu("spellcheck",a);Yu("spellcheck",a);a=new cMa;Xu("ignore_word",a);Yu("ignore_word",a);a=new bMa;Xu("date_time",a);Yu("date_time",a);a=new ZLa;Xu("comment",a);Yu("comment",a);a=new iMa;Xu("voice_corrections",a);Yu("voice_corrections",a);a=new jMa;Xu("voice_dotted_span",a);Yu("voice_dotted_span",
a);a=new aMa;Xu("composing_region",a);Yu("composing_region",a);a=new $La;Xu("composing_decoration",a);Yu("composing_decoration",a);return yLa}var yLa=null;var kMa=new Pu({17:"b_gt",36:"b_gf",37:"b_gs",28:"b_ifl",13:"b_il",29:"b_sn"}),lMa=new Pu({1:0,2:1,3:2,4:3,5:5,6:4,7:7,8:6,0:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15,16:16}),mMa={b_a:!0,b_a_i:!0},nMa=[1,2,3],oMa=null,pMa=null;function qMa(a){var b=rMa(),c=[],d;for(d in a)if(!mMa[d]){var e=a[d];"b_ts"==d?ab(c,KLa(JLa(e,"text"))):bo(b.Mf(),d)&&a[d]&&(e=co(b.Mf(),d),e=Number(ct(kMa).get(e)),c.push(e))}return c}
function sMa(a,b){var c=rMa(),d={},e;for(e in a)if(!mMa[e]){var f=a[e];switch(e){case "b_ts":f=MLa(f,"text");Kb(d,QLa(PLa(f,"text",b)));break;default:if(!bo(c.Mf(),e)){var g=eo(c.Mf(),e);if(!a[g]){var k=e;g=ct(kMa).get(k);switch(k){case "b_gt":f=Number(ct(lMa).get(String(f)))}d[g]=f}}}}return d}
function tMa(a,b,c){var d={},e={},f=!1,g;for(g in b){var k=Number(g),l=b[k];switch(k){case 17:case 36:case 37:case 28:case 13:case 29:uMa(k,l,d);break;default:f=!0,e[k]=l}}b=[];for(g=0;g<a.length;g++)switch(k=a[g],k){case 17:case 36:case 37:case 28:case 13:case 29:k=kMa.get(String(k));k=eo(rMa().Mf(),k);d[k]=!0;break;default:f=!0,b.push(k)}f&&(b=HLa(b),e=ILa(e),d.b_ts=CLa("text",b,e,null,c));d.b_a_i=!0;return d}
function uMa(a,b,c){var d=kMa.get(String(a));switch(a){case 17:a=Number(lMa.get(String(b)));break;default:a=b}c[d]=a;(d=eo(rMa().Mf(),d))&&(c[d]=!1)}function rMa(){oMa||(oMa=new cr({}));return oMa};function vMa(){}vMa.prototype.D=function(){return[]};function MGa(a,b){a=a.D(b);if(!pMa){for(var c=[],d=0;8>=d;d++){for(var e=void 0,f=d,g={},k=kMa.getKeys(),l=0;l<k.length;l++)uMa(Number(k[l]),mFa(Number(k[l])),g);uMa(28,36*(f+.5),g);uMa(13,36*(f+1),g);uMa(17,nMa[f%nMa.length],g);g.b_a=2;f=bv();k={};for(e in ELa)e=Number(e),l=32==e?null:mFa(e),k[e]=l;e=tMa([],k,f).b_ts;g.b_ts=e;c.push(new cr(g))}pMa=c}b=bd(b,0,8);b=pMa[b].clone();for(c=0;c<a.length;c++)d=a[c].clone(),b.Mr(d),b=d;return b};function wMa(a){this.zb=a}x(wMa,vMa);wMa.prototype.D=function(a){if(!(this.zb.Hb()&&this.zb.mf()&&this.zb.Vj()))return vMa.prototype.D.call(this,a);for(var b=[],c=this.zb.Hb().vf();null!=c;){a:{var d=a;var e=c.ln(this.zb.Vj());if(e&&e.Hd()&&(e=e.Jb().Ge("bodyPlaceholderListEntity"))){d=Tt(e,d);break a}d=null}d&&b.unshift(d);c=c.vf()}return b};function xMa(a){return a instanceof Xs&&a.eg()?new wMa(a):new vMa};function yMa(){}x(yMa,E);function zMa(a,b,c){c=c.Ge(a);if(!c)throw G("ne`"+F(a)).D;return Tt(c,b).H};function AMa(){}x(AMa,E);function BMa(){}x(BMa,E);function sJa(){}x(sJa,E);sJa.prototype.copyTo=h();function CMa(){DMa()}x(CMa,E);w=CMa.prototype;w.k7=da(127);w.Pn=r(null);w.nma=function(a,b){return b};w.tHa=h();w.mma=h();w.uHa=h();w.copyTo=function(a){if(!(a instanceof CMa))throw G("pe").D;};w.lma=function(){return new CMa};function DMa(){DMa=h();wn(["\u0010","\u0011","\u0012","\u001c"],!0)};var cv=new Ut({list:function(a){qGa();var b=[];for(var c=0;8>=c;c++){var d=iBa(c,!0);Q(P(),"docs-text-elei")&&(d.La=!0,d.xa=!0,d.Ea=!0,d.Ha=!0,d.Qa=!0,d.Ua=!0,d.Za=!0,d.F=7);d.H=LAa();b.push(d)}b=new Pt(b);return new St(a,b)}},{});function dv(a,b){var c={};if(!a)return c;for(var d in a){var e=!1,f=eo(b.Mf(),d);if(f){var g={};oi(g,d,a[d]);wo(b,g)?e=c[f]=!0:c[f]=!1}if(!e)if(!co(b.Mf(),d))lo(b,d)&&null!=b.getValue(d)?(e=b.getValue(d),e=dv(a[d],e),H(c,d,e)):oi(c,d,a[d]);else if(a[d])throw G("qe`"+F(d)).D;}return c};function ev(a){this.J=a}ev.prototype.D=function(a,b){switch(b.getType()){case "text":return Po(b,EMa());case "paragraph":return Po(b,FMa());default:return b}};ev.prototype.F=function(a,b,c){switch(c){case "text":return dv(b,EMa());case "paragraph":return dv(b,FMa());default:return b}};ev.prototype.H=p("J");function GMa(a){switch(a){case "text":return EMa();case "paragraph":return FMa();default:throw Error("re`"+a);}}function EMa(){if(HMa)return HMa;var a=IMa("text");return HMa=new Rq(a)}
function FMa(){if(JMa)return JMa;var a=IMa("paragraph");return JMa=new qr(a)}function IMa(a){var b=bv(),c={};for(d in Zu){var d=Number(d);if(Zu[d]==a){var e=3==d?null:mFa(d);b.D(a,d,e).D(c)}}return c}var HMa=null,JMa=null;function KMa(a){return null==a?null:qg(a)};function LMa(a,b){this.J=a;this.zb=b}x(LMa,ev);LMa.prototype.D=function(a,b,c,d,e,f){if(!MMa(this))return ev.prototype.D.call(this,a,b,c,d,e,f);a=a.ue("list",null!=f?f.wb():c);return NMa(b,this.zb.Hb().vf(),bu(a),this.zb.Vj())};LMa.prototype.F=function(a,b,c,d,e,f){if(!MMa(this))return ev.prototype.F.call(this,a,b,c,d,e,f);a=bu(a.ue("list",d));d=this.zb.Hb().vf();e={};for(b=Jb(b);null!=d;)(f=d.ln(this.zb.Vj()))&&(f=OMa(f,c,a))&&PMa(b,e,f),d=d.vf();PMa(b,e,GMa(c));return e};
function MMa(a){return!!a.zb.Hb()&&a.zb.mf()&&!!a.zb.Vj()}function NMa(a,b,c,d){if(!b)return Po(a,GMa(a.getType()));for(;b;){var e=b.ln(d);if(e)return e=OMa(e,a.getType(),c),b=NMa(e,b.vf(),c,d),Po(a,b);b=b.vf()}return Po(a,GMa(a.getType()))}function OMa(a,b,c){a=a.Jb(!0);var d=a.bb();return d.slice(0,cn(d))!=QMa?a.ue(b,1):a.ue(b,bd(c,0,8)+1)}
function PMa(a,b,c){var d=c.Va(),e={},f;for(f in d){var g=c.Mf().Da(f);if(g.F&&!d[f])g=g.F.getKey();else if(g.D)continue;else g=f;void 0!==a[g]&&(e[g]=a[g],delete a[g])}Kb(b,dv(e,c))}var QMa="\u0003"+Ec("\n",9);function RMa(a,b){this.J=a;this.O=b}x(RMa,ev);RMa.prototype.D=function(a,b){return Po(b,SMa(this))};RMa.prototype.F=function(a,b){return dv(b,SMa(this))};function SMa(a){var b=GMa(a.H()).clone(),c=bv(),d=ALa(a.O.J)[a.H()];d&&(a=ct(DLa).get(a.H()),c=CLa(a,[],d,null,c),b.update(c));return b};function TMa(a,b){return b?b instanceof Xs?b.eg()?new LMa(a,b):new ev(a):new RMa(a,b):new ev(a)};function GJa(a){for(var b={},c=["paragraph","text"],d=0;d<c.length;d++)H(b,c[d],a);return b};function UMa(){}x(UMa,E);function VMa(){}x(VMa,E);function WMa(a){this.D=a};function XMa(){}x(XMa,E);XMa.prototype.D=function(a,b,c,d){a=Cu(b);c=au(b);var e=!!c&&d.yn(c);if(!a.xt()&&!e)return d=nIa(),Vf(au(b),au(d))&&bu(b)==bu(d)||(a={},Vf(au(b),au(d))||H(a,"ls_id",au(b)),bu(b)!=bu(d)&&(a.ls_nest=bu(b)),d.Nd(a)),d;if(a&&!no(b))return b;if(!e)return b=b.clone(),d=Wq(),oIa(d).Mr(b),b;d=zMa(c,bu(b),d);b=b.clone();oIa(d).Mr(b);return b};
XMa.prototype.F=function(a,b,c,d,e){c=b.ls_ts;if(!c)return b;a=a.ue("list",d);d="ls_id"in b?b.ls_id:au(a);if(!d||!e.yn(d))return YMa(c)&&ni(b,"ls_ts"),b;c={};for(var f in b)if("ls_ts"===f){var g=dv(b[f],zMa(d,"ls_nest"in b?b.ls_nest:bu(a),e)),k=$Aa();k.Mf().J.length==Nh(g)&&wo(k,g)?ni(c,f):H(c,f,g)}else oi(c,f,b[f]);return c};XMa.prototype.H=r("list");
function YMa(a){var b=$Aa(),c=b.Mf();if(c.J.length==Nh(a)){for(var d in a){if(bo(c,d))return!1;var e=a[d],f=b.getValue(d);if(Tka(e)&&Ova(f)){if(!ZMa(f,e))return!1}else if(e!=f)return!1}return!0}return ZMa(b,a)}function ZMa(a,b){return a.Mf().D.length==Nh(b)&&wo(a,b)};function fv(a){Xs.call(this,a)}x(fv,Xs);fv.prototype.Pk=r(!0);fv.prototype.clone=function(){return Xs.prototype.clone.call(this)};fv.prototype.j4=function(){return this};fv.prototype.v4=function(){return this};function gv(a,b){b=$Ma(b);a.copyTo(b);return b}function hv(a){a=$Ma(a);a.initialize();return a}function $Ma(a){var b=[new WMa(xMa(a))],c=TMa("text",a);a=TMa("paragraph",a);c=[c,a,new XMa(new yMa)];a=a instanceof LMa?[new UMa]:[];var d=Vu(),e=[new VMa],f=KJa(),g=new CMa,k=new sJa,l=new BMa,m=new AMa;if(Q(P(),"sketchy-rssrs")){aNa||(aNa=new YIa(Uu));var n=aNa}else n=null;return new Nu(new tl(d),c,a,e,b,cv,Uu,f,g,k,l,m,n)}var bNa=null,aNa=null;function cNa(){bNa||(bNa=hv());return bNa};function iv(){this.H=[];this.F=[];this.J=[];this.D=this.R=null;this.O=!0}var dNa=[2,2,6,6,0];function jv(a,b){b.D&&(Array.prototype.push.apply(a.H,b.H),Array.prototype.push.apply(a.F,b.F),Array.prototype.push.apply(a.J,b.J),a.D=b.D.concat(),a.R=b.R.concat(),a.O=a.O&&b.O);return a}w=iv.prototype;w.clear=function(){this.H.length=0;this.F.length=0;this.J.length=0;this.D=this.R=null;this.O=!0;return this};
w.Kj=function(a,b){0==Da(this.H)?this.J.length-=2:(this.H.push(0),this.F.push(1));this.J.push(a,b);this.D=this.R=[a,b];return this};w.lineTo=function(a){return eNa(this,arguments)};function eNa(a,b){var c=Da(a.H);if(null==c)throw Error("ue");1!=c&&(a.H.push(1),a.F.push(0));for(c=0;c<b.length;c+=2){var d=b[c],e=b[c+1];a.J.push(d,e)}a.F[a.F.length-1]+=c/2;a.D=[d,e];return a}w.Eo=function(a){return fNa(this,arguments)};
function fNa(a,b){var c=Da(a.H);if(null==c)throw Error("ve");2!=c&&(a.H.push(2),a.F.push(0));for(c=0;c<b.length;c+=6){var d=b[c+4],e=b[c+5];a.J.push(b[c],b[c+1],b[c+2],b[c+3],d,e)}a.F[a.F.length-1]+=c/6;a.D=[d,e];return a}w.close=function(){var a=Da(this.H);if(null==a)throw Error("we");4!=a&&(this.H.push(4),this.F.push(1),this.D=this.R);return this};function gNa(a,b,c,d,e){var f=a.D[0]-jd(d,b)+jd(d+e,b),g=a.D[1]-ld(d,c)+ld(d+e,c);a.H.push(3);a.F.push(1);a.J.push(b,c,d,e,f,g);a.O=!1;a.D=[f,g]}
w.Qs=function(a,b,c,d){var e=this.D[0]-jd(c,a),f=this.D[1]-ld(c,b),g=hd(d);d=Math.ceil(Math.abs(g)/Math.PI*2);g/=d;c=hd(c);for(var k=0;k<d;k++){var l=Math.cos(c),m=Math.sin(c),n=4/3*Math.sin(g/2)/(1+Math.cos(g/2)),q=e+(l-n*m)*a,t=f+(m+n*l)*b;c+=g;l=Math.cos(c);m=Math.sin(c);this.Eo(q,t,e+(l+n*m)*a,f+(m-n*l)*b,e+l*a,f+m*b)}return this};function kv(a,b){for(var c=a.J,d=0,e=0,f=a.H.length;e<f;e++){var g=a.H[e],k=dNa[g]*a.F[e];b(g,c.slice(d,d+k));d+=k}}function hNa(a){return a.D&&a.D.concat()}
w.clone=function(){var a=new iv;a.H=this.H.concat();a.F=this.F.concat();a.J=this.J.concat();a.R=this.R&&this.R.concat();a.D=this.D&&this.D.concat();a.O=this.O;return a};var iNa={};iNa[0]=iv.prototype.Kj;iNa[1]=iv.prototype.lineTo;iNa[4]=iv.prototype.close;iNa[2]=iv.prototype.Eo;iNa[3]=iv.prototype.Qs;function jNa(a){if(a.O)return a.clone();var b=new iv;kv(a,function(c,d){iNa[c].apply(b,d)});return b}
iv.prototype.transform=function(a){if(!this.O)throw Error("xe");a.transform(this.J,0,this.J,0,this.J.length/2);this.R&&a.transform(this.R,0,this.R,0,1);this.D&&this.R!=this.D&&a.transform(this.D,0,this.D,0,1);return this};iv.prototype.isEmpty=function(){return 0==this.H.length};function lv(a){this.length=a.length||a;for(var b=0;b<this.length;b++)this[b]=a[b]||0}lv.prototype.BYTES_PER_ELEMENT=4;lv.prototype.set=function(a,b){b=b||0;for(var c=0;c<a.length&&b+c<this.length;c++)this[b+c]=a[c]};lv.prototype.toString=Array.prototype.join;"undefined"==typeof Float32Array&&(lv.BYTES_PER_ELEMENT=4,lv.prototype.BYTES_PER_ELEMENT=lv.prototype.BYTES_PER_ELEMENT,lv.prototype.set=lv.prototype.set,lv.prototype.toString=lv.prototype.toString,na("Float32Array",lv,void 0));function mv(a){this.length=a.length||a;for(var b=0;b<this.length;b++)this[b]=a[b]||0}mv.prototype.BYTES_PER_ELEMENT=8;mv.prototype.set=function(a,b){b=b||0;for(var c=0;c<a.length&&b+c<this.length;c++)this[b+c]=a[c]};mv.prototype.toString=Array.prototype.join;if("undefined"==typeof Float64Array){try{mv.BYTES_PER_ELEMENT=8}catch(a){}mv.prototype.BYTES_PER_ELEMENT=mv.prototype.BYTES_PER_ELEMENT;mv.prototype.set=mv.prototype.set;mv.prototype.toString=mv.prototype.toString;na("Float64Array",mv,void 0)};var kNa=Math.PI/12,lNa=hd(2),mNa=.5/3;function nNa(a,b,c,d){return[Math.min(a,c),Math.min(b,d),Math.max(a,c),Math.max(b,d)]}function nv(a,b,c){c=c||new ks;var d=ov(b)/ov(a),e=pv(b)/pv(a);c.OC(d,0,0,e,b[0]-d*a[0],b[1]-e*a[1]);return c}function qv(a){return(new iv).Kj(a[0],a[1]).lineTo(a[2],a[1]).lineTo(a[2],a[3]).lineTo(a[0],a[3]).close()}function rv(a,b){var c=new iv;c.Kj(a[0],a[1]);2<a.length&&(a=a.slice(2),eNa(c,a),b&&c.close());return c}
function sv(a){for(var b=a[0].concat(),c=1;c<a.length;c++){var d=a[c];b[0]=Math.min(b[0],d[0]);b[1]=Math.min(b[1],d[1]);b[2]=Math.max(b[2],d[2]);b[3]=Math.max(b[3],d[3])}return b}function tv(a,b){var c=a[0],d=a[1],e=a[2];a=a[3];c=[c,d,e,d,e,a,c,a];b&&b.transform(c,0,c,0,4);return c}
function uv(a){for(var b=Number.MAX_VALUE,c=Number.MAX_VALUE,d=-Number.MAX_VALUE,e=-Number.MAX_VALUE,f=0,g=a.length;f<g;f+=2){var k=a[f],l=a[f+1];b=Math.min(b,k);c=Math.min(c,l);d=Math.max(d,k);e=Math.max(e,l)}return[b,c,d,e]}function vv(a){for(var b=a.length,c=0,d=0,e=0;e<b;)c+=a[e++],d+=a[e++];return[2*c/b,2*d/b]}function oNa(a,b,c,d){a=uv(tv(a,ms(-b,0,0)));var e=ov(a),f=a[0];void 0!==c&&(a[0]=f+c*e);void 0!==d&&(a[2]=f+d*e);c=[];ms(b,0,0).transform([a[0],a[3],a[2],a[3]],0,c,0,2);return c}
function pNa(a,b,c,d,e){var f=(d[0]-c[0])*(a[1]-c[1])-(d[1]-c[1])*(a[0]-c[0]),g=(b[0]-a[0])*(a[1]-c[1])-(b[1]-a[1])*(a[0]-c[0]);c=(d[1]-c[1])*(b[0]-a[0])-(d[0]-c[0])*(b[1]-a[1]);return 0!=c&&(f/=c,g/=c,e||0<=f&&1>=f&&0<=g&&1>=g)?[a[0]+f*(b[0]-a[0]),a[1]+f*(b[1]-a[1])]:null}function ov(a){return a[2]-a[0]}function pv(a){return a[3]-a[1]}function wv(a,b){return qNa(tv(a,b))}function qNa(a){var b=xv(a.slice(0,2),a.slice(2,4));a=xv(a.slice(2,4),a.slice(4,6));return new sd(b,a)}
function yv(a,b){a=tv(a,b);return uv(a)}function rNa(a,b){a=yv(a,b);return new sd(ov(a),pv(a))}function sNa(a){for(var b=new ks,c=0;c<arguments.length;c++)ls(b,arguments[c]);return b}function zv(a){var b=[0,0,1,0];a.transform(b,0,b,0,2);return(Math.atan2(b[3]-b[1],b[2]-b[0])+2*Math.PI)%(2*Math.PI)}function tNa(a){return[(a[0]+a[2])/2,(a[1]+a[3])/2]}function uNa(a,b,c){return(b[0]-a[0])*(c[1]-b[1])>(b[1]-a[1])*(c[0]-b[0])}function xv(a,b){return Math.sqrt(Av(a,b))}
function Av(a,b){var c=a[0]-b[0];a=a[1]-b[1];return c*c+a*a}function vNa(a,b,c,d,e){if(!d)return b;a=wNa([b[0]-a[0],b[1]-a[1]]);c=wNa([c[0]-b[0],c[1]-b[1]]);c=[a[0]+c[0],a[1]+c[1]];if(0==xv([0,0],c))return[b[0]+a[0]*d,b[1]+a[1]*d];c=wNa(c);c=[-c[1],c[0]];a=[-a[1],a[0]];d/=a[0]*c[0]+a[1]*c[1];e&&(isNaN(d)||d>e)&&(d=e);return[b[0]+c[0]*d,b[1]+c[1]*d]}function wNa(a){var b=xv([0,0],a);return[a[0]/b,a[1]/b]}
function xNa(a,b,c){var d=b[0]-a[0];b=b[1]-a[1];var e=d*d+b*b;if(0==e)throw Error("ze");a=a[1]*d-a[0]*b;c=c[0]*d+c[1]*b;return[(d*c-b*a)/e,(b*c+d*a)/e]}function yNa(a,b){b=zNa(b);a=zNa(a);ls(b,rs(a));return b}function zNa(a){return new ks(a[2]-a[0],a[3]-a[1],a[4]-a[0],a[5]-a[1],a[0],a[1])}function ANa(a){return 1==a.Cg&&0==a.Hh&&0==a.Uh&&1==a.gg}
function BNa(a,b,c){var d=c||mNa,e=a.length;if(6>e)return rv(a,b);c=[];for(var f=0;f<e;f+=2){var g=f+2,k=f-2;g==e&&(g=b?0:e-2);0>k&&(k=b?e-2:0);c[f]=d*(a[g]-a[k]);c[f+1]=d*(a[g+1]-a[k+1])}d=e-2;e=new iv;e.Kj(a[0],a[1]);for(f=0;f<d;f+=2)e.Eo(a[f]+c[f],a[f+1]+c[f+1],a[f+2]-c[f+2],a[f+3]-c[f+3],a[f+2],a[f+3]);b&&(e.Eo(a[d]+c[d],a[d+1]+c[d+1],a[0]-c[0],a[1]-c[1],a[0],a[1]),e.close());return e}function CNa(a,b,c,d,e,f){e=[e,f];return Av(e,xNa([a,b],[c,d],e))}
function DNa(a,b,c,d,e,f,g,k){return a==g&&b==k?Math.sqrt(Math.max(Av([a,b],[c,d]),Av([a,b],[e,f]))):Math.sqrt(Math.max(CNa(a,b,g,k,c,d),CNa(a,b,g,k,e,f)))}function ENa(a,b){if(8!=a.length)throw Error("Ae`"+Math.floor(a.length/2));var c=a[0],d=a[1],e=a[2],f=a[3],g=a[4],k=a[5],l=a[6];a=a[7];var m=(e+g)/2,n=(f+k)/2;e=(c+e)/2;f=(d+f)/2;g=(l+g)/2;k=(a+k)/2;var q=(e+m)/2,t=(f+n)/2;m=(g+m)/2;n=(k+n)/2;b.splice(0,14,c,d,e,f,q,t,(q+m)/2,(t+n)/2,m,n,g,k,l,a)}
function FNa(a,b,c){a=jNa(a);var d=void 0!==c?c:10;if(0>d)throw Error("Be`"+d);var e=new iv;kv(a,function(f,g){switch(f){case 4:e.close();break;case 0:e.Kj(g[0],g[1]);break;case 1:eNa(e,g);break;case 2:f=hNa(e);if(!f)throw Error("Ce");for(var k=0;k<g.length;k+=6)Array.prototype.push.apply(f,g.slice(k,k+6));g=f;for(f=d;0<f--;){k=[g[0],g[1]];for(var l=2,m=!1;l<g.length;){var n=k.length;n=[k[n-2],k[n-1],g[l++],g[l++],g[l++],g[l++],g[l++],g[l++]];DNa.apply(null,n)>b&&(ENa(n,n),m=!0);n.splice(0,2);Array.prototype.push.apply(k,
n)}g=k;if(!m)break}g.splice(0,2);fNa(e,g);break;default:throw Error("De`"+f);}});return e}function Bv(a,b,c){for(var d=[],e=0;e<a.length;e++){var f=a[e];d.push(c?(Math.floor(f/b)+.5)*b:Math.round(f/b)*b)}return d}
function Cv(a,b){var c=new iv;kv(a,function(d,e){var f=e?Bv(e,b,!0):e;switch(d){case 0:c.Kj(f[0],f[1]);break;case 1:eNa(c,f);break;case 2:for(d=0;d<e.length;d+=6)c.Eo(e[d],e[d+1],e[d+2],e[d+3],f[d+4],f[d+5]);break;case 3:for(d=0;d<e.length;d+=6)gNa(c,f[d],f[d+1],e[d+2],e[d+3]);break;case 4:c.close()}});return c};function Dv(a,b){Xs.call(this,a);this.F=b;this.Sd={};this.H=this.J=this.D=null}x(Dv,fv);w=Dv.prototype;w.ww=function(){return new Dv(this.getId(),this.F)};w.eg=r(!0);w.getType=p("F");function GNa(a,b){for(var c=0;7>=c;c++)delete a.Sd[c];c=tv(a.Se(),a.transform);a.F=b;a.transform.Gn(yNa(tv(a.Se()),c))}w.mb=p("Sd");w.hs=function(a){return a in this.Sd};w.Da=function(a){return st(this.Sd,a,this.getType())};w.setProperty=function(a,b){this.Sd[a]=b};w.Kv=da(129);function Ev(a){return 0==Iv(a)}
function Iv(a){a.Hd()?(a=a.Jb().bb(),a=a.slice(1,cn(a)-2)):a=a.Da(33)||"";return a.leng