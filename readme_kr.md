NOT updated (2024-08-02)

RCTFN은 파일 구성을 더 편리하게 하기 위해 만들어진 간단한 파이썬 스크립트입니다.

[한국어 버전](https://github.com/oil-lamp-cat/Rename-Contents-To-Folder-Name/blob/1.0.0/readme_kr.md)과 [영어 버전](https://github.com/oil-lamp-cat/Rename-Contents-To-Folder-Name/blob/1.0.0/readme.md)이 있습니다.

dist 폴더에서 main_language.py를 실행할 수 있습니다.

테스트 폴더가 아래와 같이 구성되어 있다고 했을 때

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

1. 폴더에 여러 개의 폴더가 있는 경우 폴더의 이름이 아닌 내부 폴더의 파일 내용은 다음과 같이 이름이 바뀝니다.

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

2. 첫 번째 단계의 폴더에 있는 내용의 이름을 변경합니다. 예를 다시 테스트 파일로 사용하면 다음과 같이 변경됩니다

```
D:.
|   Test_1.txt
|   Test_3.txt
|   테스트_5.txt
|
+---테스트_0
|       test1_0.txt
|       test1_1.txt
|       test1_2.txt
|
+---테스트_2
|       test2_0.txt
|       test2_1.txt
|       test2_2.txt
|
+---테스트_4
|       test3_0.txt
|       test3_1.txt
|       test3_2.txt
|
\---테스트_6
        test4_0.txt
        test4_1.txt
        test4_2.txt
```

아직 다른 기능을 구현할 계획은 없습니다.