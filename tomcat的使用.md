# tomcat简洁 #
一个轻量级的web服务器。web服务器是一个应用程序（软件/),对HTTP协议的操作进行封装，让程序员不必对协议进行操作，让web开发更便捷
#启动#
bin中，双击startup.bat
#关闭#
ctrl+c(正常关闭，推荐)
直接×掉窗口（不推荐）
bin中，双击shuttingdown.bat
#修改端口号#
con/sever.xml进行修改
符合0~65535即可
#bin#
即binnary,存放二进制文件，即一些可执行文件
#conf#
存放配置文件
#lib#
tomcat依赖的jar包
#logs#
日志文件
#temp#
临时文件
#web apps#
应用发布目录（即部署项目的地方）
注意：要在这个文件夹下新建一个文件夹，再把东西放进去，比方说，在webapp下新建一个hello文件夹，在里面放了一个mybatis2.png,访问的时候，localhost：8080/hello/mybatis.png即可。
注意：如果项目比较大，可以打包成一个war包，放到webapp下，会自动解压缩，再正常访问即可。
#work#
工作目录
