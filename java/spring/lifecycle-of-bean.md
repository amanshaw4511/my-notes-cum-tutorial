
-> Read Configuratin file
-> Set properties of bean
-> setBeanName
-> setBeanFactory/ setApplicationContext
-> PostProcessBeforeInitialization
-> @PostConstruct
-> InitializingBean interface (afterPropertySet())
-> custom 'init' method
-> PostProcessAfterInitialization
-> Bean is ready

-> Spring Container shutdown
-> @PreDestroy
-> DisposableBean interface (destroy())
-> custome 'destroy' method
-> end




# Bean lifecycle
by default spring gives us two method for every bean

- public void init()
- public void destroy()


# we can change name and use annotation instead
@PostConstruct
@PreDestroy
