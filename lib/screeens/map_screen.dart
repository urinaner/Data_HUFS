import 'package:flutter/material.dart';

class MapScreen extends StatefulWidget {
  const MapScreen({super.key});

  @override
  State<MapScreen> createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> {
  @override
  Widget build(BuildContext ctx) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('근처 대피소'),
      ),
      body: Center(
          child: ElevatedButton(
        child: const Text('gd'),
        onPressed: () {
          Navigator.pop(ctx);
        },
      )),
    );
  }
}
