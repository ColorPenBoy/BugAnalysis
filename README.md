# BugAnalysis
根据Umeng提供的内存地址dSYM文件，定位bug，半自动化脚本

集成了Umeng（或其它bug tracker SDK）的项目中，如何追踪定位那些测试部门没有测出来，复现难度大，隐藏比较深的bug呢？

### 记录操作步骤
1、Archive之后，每个上线的版本都会在Xcode中留下一个`YourProject.xcarchive`文件存档记录。（仅限于使用Xcode进行Archive并Submit的，使用CI server等方式进行自动打包可以自行保留）

如何找到它呢：`Xcode -> Window -> Organizer -> Archives`，可以看到一排都是`.xcarchive`文件

2、选中此次提交的版本（一般最顶端那个就是），`右键 -> Show in Finder`

3、将`YourProject.xcarchive`文件粘贴到某个自己新建的bugFile文件夹中（文件夹命名随意、路径随意）

4、`YourProject.xcarchive右键 -> 显示包内容 -> dSYMs文件夹 -> 复制 YourProject.app.dSYM 文件到bugFile文件夹中`

5、`YourProject.app.dSYM 右键 -> 显示包内容 -> Contents -> Resources -> DWARF -> 复制 YourProject 文件到bugFile文件夹中`

6、此时放入文件夹中3个文件：
	
* `YourProject.xcarchive` 
* `YourProject.app.dSYM` 
* `YourProject`

7、文件夹中放入项目中的两个文件

* `BugTracker.py`
* `BugAddressList`

8、在`BugTracker.py`文件中，将project_name修改为你自己的项目名称

9、所有Umeng（或其它平台）后台收集到的crash 内存地址，全部粘贴到`BugAddressList`文件中（每行粘贴一个内存地址，回车换行）

10、打开终端，cd到 bugFile 中，输入命令`$ python BugTracker.py` 即可看到控制台打印出的定位记录。