web server 开发框架

使用方法：

          1,./web -h 查看帮助说明, -s  自定义接口python脚本 -p  服务占用端口

          2,自定义脚本内必须包含一个主函数method_name(args={})，函数输入为dict，输出为json字符串，文件名 SERVICE_NAME.py

          3，服务访问形式http://127.0.0.1:PORT/SERVICE_NAME?method=method_name&name=Test

          4，服务上线需要通知管理员夏季添加到nginx

测试用例：

          1,编写脚本test.py，脚本包含函数 get_name(args{}),函数参数统一以dict传入，返回json字符串

          2,后台运行 ./web -s test.py -p 30010
          
          3,访问接口 http://127.0.0.1:30010/test?method=get_name&name=Test
 
