function map2obj(map) {
   var res = {};
   var keyset = map.keySet();
   var it = keyset.iterator();
   while (it.hasNext()) {
      var keystr = it.next().toString();
      var valuestr = map.get(keystr).toString();
      res[keystr] = valuestr
   }
   return res;
}

function dfs(self, depth) {
    if (depth > 6) return {}
    const obj = {}
    const cls = self.getClass()
    const fields = cls.getDeclaredFields()
    // console.log("-".repeat(depth), "dfs", cls, self)
    // console.log("-".repeat(depth), "fields:", fields)
    const immediates = ['short', 'int', 'long', 'float', 'double', 'boolean', 'String']
    fields.forEach(x => {
        x.setAccessible(true)
        const v = x.get(self)
        if (v === null) return
        const s = x.toString()  // public type fullname
        // const type = x.getType()   // class java.lang.String
        // const k = x.getName()   // short name
        // console.warn(x, v, k, type)
        if (immediates.some(type => s.includes(type))) {
            obj[x] = v.toString()
        } else {  // inner class
            obj[x] = dfs(v, depth+1)
        }
    })
    return obj
}

function hookJava() {
   if (Java.available) {
      Java.perform(function () {
         var cls = Java.classFactory.use("com.package.classname");
         cls.methodName.implementation = function (a1, a2, a3, a4) {
            console.log('-'.repeat(10), "start Java hook")
            let a2str = JSON.stringify(map2obj(a2), null, 4)
            console.log(a1, a3, a4)
            console.warn(a2str)
            var res = this.methodName(a1, a2, a3, a4)
            console.warn('res:', res)
            return res
         }
      })
   }
}

function hookNative() {
   let m = Process.findModuleByName('lib.so')
   let f = Module.findExportByName('lib.so', 'Functions_xx')
   console.log(m.base, f)
   Interceptor.attach(f, {
      onEnter: function (args) {
         console.warn("args:", args[1], args[1].readCString())
      },
      onLeave: function (ret) {
         console.warn("ret:", ret, ret.readCString())
      }
   })
}

setImmediate(hookJava)
// setImmediate(hookNative)