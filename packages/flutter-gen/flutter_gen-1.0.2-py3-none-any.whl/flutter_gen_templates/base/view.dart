import 'package:flutter/material.dart';
import 'package:pt_flutter_architecture/pt_flutter_architecture.dart';
import 'package:{{ package_name }}/core/architecture/mobx_obs.dart';
import 'package:{{ package_name }}/core/architecture/mobx_view.dart';

import '{{ name_lower }}_viewmodel.dart';

class {{ name }}Binding implements Bindings {
  @override
  void dependencies() {
    Get.put<{{ name }}SceneUseCaseType>({{ name }}SceneUseCase());
    Get.put<{{ name }}Navigator>({{ name }}Navigator());
    Get.put<{{ name }}ViewModel>({{ name }}ViewModel());
  }
}

class {{ name }}View extends MobXView<{{ name }}ViewModel> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(),
    );
  }
}
