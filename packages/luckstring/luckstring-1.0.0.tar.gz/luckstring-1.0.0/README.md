luckdog是类似于内置函数split的方法，扩展支持了分割符号忽略大小写特征的分割。


使用说明：

1） 安装：

    pip install luckstring

2） 执行
    
    from luckstring import luckstring
    string = "`product_group_id` VARCHAR(64) NULL DEFAULT NULL comment '产品组的ID'"
    luckstring.split(string, "COMMENT") 


## 注： 为方便后期操作方便 

# 可以 把上面的 运行命令放到bat或shell文件中，下次直接双击运行 

#######################################################################

Last update time: 2022-04-01 

By： 9034.com

#######################################################################

更新日志：
2022-04-01  v1.0.0  初始化


#######################################################################
## 打包步骤
    ## 打包 检查
    python setup.py check 
    ## 打包 生成
    python setup.py sdist
    ## 上传
    twine upload dist/*
    ## 使用
    pip install luckstring
    ## 更新
    pip install --upgrade luckstring
    ## 卸载
    pip uninstall -y luckstring 
#######################################################################

## MANIFEST.in 配置教程

    include pat1 pat2 ...   #include all files matching any of the listed patterns

    exclude pat1 pat2 ...   #exclude all files matching any of the listed patterns

    recursive-include dir pat1 pat2 ...  #include all files under dir matching any of the listed patterns

    recursive-exclude dir pat1 pat2 ... #exclude all files under dir matching any of the listed patterns

    global-include pat1 pat2 ...    #include all files anywhere in the source tree 
    matching — & any of the listed patterns

    global-exclude pat1 pat2 ...    #exclude all files anywhere in the source tree matching — & any of the listed patterns

    prune dir   #exclude all files under dir

    graft dir   #include all files under dir
