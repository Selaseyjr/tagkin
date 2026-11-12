import { PRODUCT_NAME } from "@tagkin/shared";
import { tokens } from "@tagkin/tokens";
import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View, useColorScheme } from "react-native";

// Placeholder until M3 (app shell). Proves the workspace wiring and the theme tokens.
export default function App() {
  const c = tokens.color[useColorScheme() === "dark" ? "dark" : "light"];
  return (
    <View style={[styles.container, { backgroundColor: c.bg }]}>
      <Text style={[styles.title, { color: c.ink }]}>{PRODUCT_NAME}</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: "center", justifyContent: "center" },
  title: { fontSize: tokens.text.xl, fontWeight: "700" },
});
