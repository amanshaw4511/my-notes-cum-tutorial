# PointCut

class CommonPointcutConfig {
    @Pointcut("execution(* com.aman.data.*.*(..))")
    public void dataLayerExecution() {}
}

@Configuration
@Aspect
class Aspect {
    @Before("com.aman.aop.CommonPointcutConfig.dataLayerExecution")
    public void before(JoinPoint joinPoint) {
        String methodName = joinPoint.getSignature().getName();
        System.out.println("before " + methodName);
    }
}
```
