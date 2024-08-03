RCTFN is just a Python script made to make file organization more convenient.

There is a [Korean version](https://github.com/oil-lamp-cat/Rename-Contents-To-Folder-Name/blob/1.0.0/readme_kr.md) and an [English version](https://github.com/oil-lamp-cat/Rename-Contents-To-Folder-Name/blob/1.0.0/readme.md).

You can run the main_language.py in the dist folder.

When you say that the test folder is structured as below

```
D:.
|   test1.txt
|   test2.txt
|   test3.txt
|
+---test1
|       test1.txt
|       test2.txt
|       test3.txt
|
+---test2
|       test1.txt
|       test2.txt
|       test3.txt
|
+---test3
|       test1.txt
|       test2.txt
|       test3.txt
|
\---test4
        test1.txt
        test2.txt
        test3.txt
```

1. When there are multiple folders in the folder, the contents of the file in the inner folder, not the name of the folder, are renamed as follows.

```
D:.
|   test1.txt
|   test2.txt
|   test3.txt
|
+---test1
|       test1_0.txt
|       test1_1.txt
|       test1_2.txt
|
+---test2
|       test2_0.txt
|       test2_1.txt
|       test2_2.txt
|
+---test3
|       test3_0.txt
|       test3_1.txt
|       test3_2.txt
|
\---test4
        test4_0.txt
        test4_1.txt
        test4_2.txt
```

2. You will rename the contents in the folder of the first step. If you take an example as a test file again, it will change as follows

```
D:.
|   Test_1.txt
|   Test_3.txt
|   Test_5.txt
|
+---Test_0
|       test1_0.txt
|       test1_1.txt
|       test1_2.txt
|
+---Test_2
|       test2_0.txt
|       test2_1.txt
|       test2_2.txt
|
+---Test_4
|       test3_0.txt
|       test3_1.txt
|       test3_2.txt
|
\---Test_6
        test4_0.txt
        test4_1.txt
        test4_2.txt
```

3. works same as `1` but this time it will not delete contents name, it will add after the new name.

D:.
│  test1.txt
│  test2.txt
│  test3.txt
│
├─test1
│      test1_0_test1_.txt
│      test1_1_test2_.txt
│      test1_2_test3_.txt
│
├─test2
│      test2_0_test1_.txt
│      test2_1_test2_.txt
│      test2_2_test3_.txt
│
├─test3
│      test3_0_test1_.txt
│      test3_1_test2_.txt
│      test3_2_test3_.txt
│
└─test4
        test4_0_test1_.txt
        test4_1_test2_.txt
        test4_2_test3_.txt

There are no plans to implement any other functions yet.