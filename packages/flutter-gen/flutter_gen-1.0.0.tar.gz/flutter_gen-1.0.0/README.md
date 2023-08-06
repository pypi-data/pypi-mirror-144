# Code generator for Flutter apps
## Installation:

#### Install Python on Mac
```
$ brew install python3
```

#### Install Python on Windows
```
https://www.python.org/downloads/
```

#### Install Tool:
```
$ pip3 install flutter_gen
```

<details>
<summary><b>Command line</b></summary>
  #### Update:
  ```
  $ pip3 install -U flutter_gen
  ```
  #### Uninstall:
  ```
  $ pip3 uninstall flutter_gen
  ```

</details>

## Generate
### 1. Generate image class:
```
$ flutter_gen gen image
```
<details>
<summary>📑 Example</summary>

```dart
const _assetsImagePath = 'assets/images';

class Images {
  static const test = '$_assetsImagePath/test.png';
}
```
</details>

### 2. Generate localization class:
```
$ flutter_gen gen localization
```
<details>
<summary>📑 Example</summary>

```dart
class i18n {
  static String get test => 'test'.tr();
}
```
</details>

### 3. Generate router class:
```
$ flutter_gen gen router
```
<details>
<summary>📑 Example</summary>

```dart
Future? toHome({int? id}) {}

Future? offAllHome({int? id}) {}

Future? offAndToHome({int? id}) {}

Future? offHome({int? id}) {}

Future? offUntilHome({int? id}) {}
```
</details>

### 4. Sync:
#### Run all generate command
```
$ flutter_gen sync
```