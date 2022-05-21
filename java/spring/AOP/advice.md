# Advices

## Before

```
@Configuration
@Aspect
class Aspect {
    @Before("execution (* com.aman.*.*(..))")
    public void before(JoinPoint joinPoint) {
        String methodName = joinPoint.getSignature().getName();
        System.out.println("before " + methodName);
    }
}
```

## After
```
@Configuration
@Aspect
class Aspect {
    @After(value = "execution (* com.aman.*.*(..))")
    public void afterThrowOrReturn(JoinPoint joinPoint) {
        String methodName = joinPoint.getSignature().getName();
        System.out.println("after " + methodName);
    }
}
```

## AfterReturning
```
@Configuration
@Aspect
class Aspect {
    @AfterReturning(
        value = "execution (* com.aman.*.*(..))",
        returning = "obj"
    )
    public void afterReturn(JoinPoint joinPoint, Object obj) {
        String methodName = joinPoint.getSignature().getName();
        System.out.println(methodName + "returned : " + obj);
    }
}
```

## AfterThrowing
```
@Configuration
@Aspect
class Aspect {
    @AfterThrowing(
        value = "execution (* com.aman.*.*(..))",
        throwing = "exception"
    )
    public void afterThrow(JoinPoint joinPoint, Exception exception) {
        String methodName = joinPoint.getSignature().getName();
        System.out.println(methodName + "throwing : " + exception);
    }
}
```



## Around
```
@Configuration
@Aspect
class Aspect {
    @Around("execution (* com.aman.*.*(..))")
    public void before(ProceeedingJoinPoint proceedingJoinPoint) {
        String methodName = proceedingjoinPoint.getSignature().getName();
        System.out.println("before " + methodName);

        proceedingJoinPoint.proceed()

        System.out.println("before " + methodName);
    }
}
```
