import 'package:flutter/material.dart';

class NewsScreen extends StatelessWidget {
  const NewsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('뉴스'),
      ),
      body: Center(
        child: ElevatedButton(
          child: const Text('gd'),
          onPressed: () {},
        ),
      ),
    );
  }
}
