
export type Json = string | number | boolean | null | { [key: string]: Json | undefined } | Json[]

export type Database = {
  
  "public": {
          Tables: {
            "abuse_reports": {
                  Row: {
                    "created_at": string,"details": string | null,"id": string,"reason": string,"reporter_account": string | null,"reporter_kind": string,"state": string,"target_id": string,"target_kind": string
                  }
                  ComputedFields: never
                  Insert: {
                    "created_at"?: string,"details"?: string | null,"id"?: string,"reason": string,"reporter_account"?: string | null,"reporter_kind": string,"state"?: string,"target_id": string,"target_kind": string
                  }
                  Update: {
                    "created_at"?: string,"details"?: string | null,"id"?: string,"reason"?: string,"reporter_account"?: string | null,"reporter_kind"?: string,"state"?: string,"target_id"?: string,"target_kind"?: string
                  }
                  Relationships: [
                    {
      foreignKeyName: "abuse_reports_reporter_account_fkey"
      columns: ["reporter_account"]
isOneToOne: false
      referencedRelation: "profiles"
      referencedColumns: ["id"]
    }
                  ]
                },"contacts": {
                  Row: {
                    "account_id": string,"alert_after_minutes": number,"email": string | null,"id": string,"name": string,"phone": string | null
                  }
                  ComputedFields: never
                  Insert: {
                    "account_id": string,"alert_after_minutes"?: number,"email"?: string | null,"id"?: string,"name": string,"phone"?: string | null
                  }
                  Update: {
                    "account_id"?: string,"alert_after_minutes"?: number,"email"?: string | null,"id"?: string,"name"?: string,"phone"?: string | null
                  }
                  Relationships: [
                    {
      foreignKeyName: "contacts_account_id_fkey"
      columns: ["account_id"]
isOneToOne: false
      referencedRelation: "profiles"
      referencedColumns: ["id"]
    }
                  ]
                },"devices": {
                  Row: {
                    "account_id": string,"id": string,"last_seen": string,"platform": string,"push_token": string | null
                  }
                  ComputedFields: never
                  Insert: {
                    "account_id": string,"id"?: string,"last_seen"?: string,"platform": string,"push_token"?: string | null
                  }
                  Update: {
                    "account_id"?: string,"id"?: string,"last_seen"?: string,"platform"?: string,"push_token"?: string | null
                  }
                  Relationships: [
                    {
      foreignKeyName: "devices_account_id_fkey"
      columns: ["account_id"]
isOneToOne: false
      referencedRelation: "profiles"
      referencedColumns: ["id"]
    }
                  ]
                },"entitlements": {
                  Row: {
                    "account_id": string,"id": string,"key": string,"source": string,"valid_until": string | null
                  }
                  ComputedFields: never
                  Insert: {
                    "account_id": string,"id"?: string,"key": string,"source": string,"valid_until"?: string | null
                  }
                  Update: {
                    "account_id"?: string,"id"?: string,"key"?: string,"source"?: string,"valid_until"?: string | null
                  }
                  Relationships: [
                    {
      foreignKeyName: "entitlements_account_id_fkey"
      columns: ["account_id"]
isOneToOne: false
      referencedRelation: "profiles"
      referencedColumns: ["id"]
    }
                  ]
                },"items": {
                  Row: {
                    "care_notes": string | null,"description": string | null,"finder_message": string,"finder_message_lang": string,"name": string,"photo_path": string | null,"tag_code": string,"temperament": (string)[] | null,"trip": Json | null,"updated_at": string
                  }
                  ComputedFields: never
                  Insert: {
                    "care_notes"?: string | null,"description"?: string | null,"finder_message": string,"finder_message_lang"?: string,"name": string,"photo_path"?: string | null,"tag_code": string,"temperament"?: (string)[] | null,"trip"?: Json | null,"updated_at"?: string
                  }
                  Update: {
                    "care_notes"?: string | null,"description"?: string | null,"finder_message"?: string,"finder_message_lang"?: string,"name"?: string,"photo_path"?: string | null,"tag_code"?: string,"temperament"?: (string)[] | null,"trip"?: Json | null,"updated_at"?: string
                  }
                  Relationships: [
                    {
      foreignKeyName: "items_tag_code_fkey"
      columns: ["tag_code"]
isOneToOne: true
      referencedRelation: "tags"
      referencedColumns: ["code"]
    }
                  ]
                },"messages": {
                  Row: {
                    "body": string,"created_at": string,"delivered_via": string | null,"id": string,"original_lang": string | null,"original_text": string | null,"return_id": string,"sender": Database["public"]['Enums']["message_sender"],"status": string,"translated_lang": string | null
                  }
                  ComputedFields: never
                  Insert: {
                    "body": string,"created_at"?: string,"delivered_via"?: string | null,"id"?: string,"original_lang"?: string | null,"original_text"?: string | null,"return_id": string,"sender": Database["public"]['Enums']["message_sender"],"status"?: string,"translated_lang"?: string | null
                  }
                  Update: {
                    "body"?: string,"created_at"?: string,"delivered_via"?: string | null,"id"?: string,"original_lang"?: string | null,"original_text"?: string | null,"return_id"?: string,"sender"?: Database["public"]['Enums']["message_sender"],"status"?: string,"translated_lang"?: string | null
                  }
                  Relationships: [
                    {
      foreignKeyName: "messages_return_id_fkey"
      columns: ["return_id"]
isOneToOne: false
      referencedRelation: "returns"
      referencedColumns: ["id"]
    }
                  ]
                },"ownership_transfers": {
                  Row: {
                    "created_at": string,"from_account": string,"id": string,"state": string,"tag_code": string,"to_email": string,"token_hash": string
                  }
                  ComputedFields: never
                  Insert: {
                    "created_at"?: string,"from_account": string,"id"?: string,"state"?: string,"tag_code": string,"to_email": string,"token_hash": string
                  }
                  Update: {
                    "created_at"?: string,"from_account"?: string,"id"?: string,"state"?: string,"tag_code"?: string,"to_email"?: string,"token_hash"?: string
                  }
                  Relationships: [
                    {
      foreignKeyName: "ownership_transfers_from_account_fkey"
      columns: ["from_account"]
isOneToOne: false
      referencedRelation: "profiles"
      referencedColumns: ["id"]
    },{
      foreignKeyName: "ownership_transfers_tag_code_fkey"
      columns: ["tag_code"]
isOneToOne: false
      referencedRelation: "tags"
      referencedColumns: ["code"]
    }
                  ]
                },"prices": {
                  Row: {
                    "amount_cents": number,"colour": string | null,"currency": string,"id": string,"market": string,"product": Database["public"]['Enums']["product"],"valid_from": string
                  }
                  ComputedFields: never
                  Insert: {
                    "amount_cents": number,"colour"?: string | null,"currency"?: string,"id"?: string,"market"?: string,"product": Database["public"]['Enums']["product"],"valid_from"?: string
                  }
                  Update: {
                    "amount_cents"?: number,"colour"?: string | null,"currency"?: string,"id"?: string,"market"?: string,"product"?: Database["public"]['Enums']["product"],"valid_from"?: string
                  }
                  Relationships: [
                    
                  ]
                },"profiles": {
                  Row: {
                    "appearance": string,"backup_email": string | null,"created_at": string,"id": string,"language": string,"recovery_phone": string | null
                  }
                  ComputedFields: never
                  Insert: {
                    "appearance"?: string,"backup_email"?: string | null,"created_at"?: string,"id": string,"language"?: string,"recovery_phone"?: string | null
                  }
                  Update: {
                    "appearance"?: string,"backup_email"?: string | null,"created_at"?: string,"id"?: string,"language"?: string,"recovery_phone"?: string | null
                  }
                  Relationships: [
                    
                  ]
                },"reports": {
                  Row: {
                    "address": string | null,"created_at": string,"finder_contact": string | null,"finder_contact_kind": string,"id": string,"lang": string,"lat": number | null,"lng": number | null,"note": string | null,"photo_path": string | null,"place_text": string | null,"return_id": string,"tag_code": string,"token_hash": string,"where_now": Database["public"]['Enums']["where_now"]
                  }
                  ComputedFields: never
                  Insert: {
                    "address"?: string | null,"created_at"?: string,"finder_contact"?: string | null,"finder_contact_kind"?: string,"id"?: string,"lang"?: string,"lat"?: number | null,"lng"?: number | null,"note"?: string | null,"photo_path"?: string | null,"place_text"?: string | null,"return_id": string,"tag_code": string,"token_hash": string,"where_now": Database["public"]['Enums']["where_now"]
                  }
                  Update: {
                    "address"?: string | null,"created_at"?: string,"finder_contact"?: string | null,"finder_contact_kind"?: string,"id"?: string,"lang"?: string,"lat"?: number | null,"lng"?: number | null,"note"?: string | null,"photo_path"?: string | null,"place_text"?: string | null,"return_id"?: string,"tag_code"?: string,"token_hash"?: string,"where_now"?: Database["public"]['Enums']["where_now"]
                  }
                  Relationships: [
                    {
      foreignKeyName: "reports_return_id_fkey"
      columns: ["return_id"]
isOneToOne: false
      referencedRelation: "returns"
      referencedColumns: ["id"]
    },{
      foreignKeyName: "reports_tag_code_fkey"
      columns: ["tag_code"]
isOneToOne: false
      referencedRelation: "tags"
      referencedColumns: ["code"]
    }
                  ]
                },"returns": {
                  Row: {
                    "closed_at": string | null,"handover_code_hash": string | null,"id": string,"opened_at": string,"state": Database["public"]['Enums']["return_state"],"tag_code": string
                  }
                  ComputedFields: never
                  Insert: {
                    "closed_at"?: string | null,"handover_code_hash"?: string | null,"id"?: string,"opened_at"?: string,"state"?: Database["public"]['Enums']["return_state"],"tag_code": string
                  }
                  Update: {
                    "closed_at"?: string | null,"handover_code_hash"?: string | null,"id"?: string,"opened_at"?: string,"state"?: Database["public"]['Enums']["return_state"],"tag_code"?: string
                  }
                  Relationships: [
                    {
      foreignKeyName: "returns_tag_code_fkey"
      columns: ["tag_code"]
isOneToOne: false
      referencedRelation: "tags"
      referencedColumns: ["code"]
    }
                  ]
                },"scans": {
                  Row: {
                    "at": string,"city": string | null,"id": number,"is_test": boolean,"report_id": string | null,"tag_code": string,"user_agent_class": string | null
                  }
                  ComputedFields: never
                  Insert: {
                    "at"?: string,"city"?: string | null,"id"?: never,"is_test"?: boolean,"report_id"?: string | null,"tag_code": string,"user_agent_class"?: string | null
                  }
                  Update: {
                    "at"?: string,"city"?: string | null,"id"?: never,"is_test"?: boolean,"report_id"?: string | null,"tag_code"?: string,"user_agent_class"?: string | null
                  }
                  Relationships: [
                    {
      foreignKeyName: "scans_report_id_fkey"
      columns: ["report_id"]
isOneToOne: false
      referencedRelation: "reports"
      referencedColumns: ["id"]
    },{
      foreignKeyName: "scans_tag_code_fkey"
      columns: ["tag_code"]
isOneToOne: false
      referencedRelation: "tags"
      referencedColumns: ["code"]
    }
                  ]
                },"status_updates": {
                  Row: {
                    "body": string,"expires_at": string,"id": string,"tag_code": string,"visible": boolean
                  }
                  ComputedFields: never
                  Insert: {
                    "body": string,"expires_at"?: string,"id"?: string,"tag_code": string,"visible"?: boolean
                  }
                  Update: {
                    "body"?: string,"expires_at"?: string,"id"?: string,"tag_code"?: string,"visible"?: boolean
                  }
                  Relationships: [
                    {
      foreignKeyName: "status_updates_tag_code_fkey"
      columns: ["tag_code"]
isOneToOne: false
      referencedRelation: "tags"
      referencedColumns: ["code"]
    }
                  ]
                },"tag_members": {
                  Row: {
                    "account_id": string,"added_at": string,"role": Database["public"]['Enums']["member_role"],"tag_code": string
                  }
                  ComputedFields: never
                  Insert: {
                    "account_id": string,"added_at"?: string,"role"?: Database["public"]['Enums']["member_role"],"tag_code": string
                  }
                  Update: {
                    "account_id"?: string,"added_at"?: string,"role"?: Database["public"]['Enums']["member_role"],"tag_code"?: string
                  }
                  Relationships: [
                    {
      foreignKeyName: "tag_members_account_id_fkey"
      columns: ["account_id"]
isOneToOne: false
      referencedRelation: "profiles"
      referencedColumns: ["id"]
    },{
      foreignKeyName: "tag_members_tag_code_fkey"
      columns: ["tag_code"]
isOneToOne: false
      referencedRelation: "tags"
      referencedColumns: ["code"]
    }
                  ]
                },"tags": {
                  Row: {
                    "activation_pin_hash": string | null,"code": string,"colour": string | null,"created_at": string,"finish": string | null,"is_free": boolean,"label": string | null,"lost_at": string | null,"product": Database["public"]['Enums']["product"],"retired_at": string | null,"size": string | null,"state": Database["public"]['Enums']["tag_state"],"test_until": string | null,"type": Database["public"]['Enums']["tag_type"] | null
                  }
                  ComputedFields: never
                  Insert: {
                    "activation_pin_hash"?: string | null,"code": string,"colour"?: string | null,"created_at"?: string,"finish"?: string | null,"is_free"?: boolean,"label"?: string | null,"lost_at"?: string | null,"product": Database["public"]['Enums']["product"],"retired_at"?: string | null,"size"?: string | null,"state": Database["public"]['Enums']["tag_state"],"test_until"?: string | null,"type"?: Database["public"]['Enums']["tag_type"] | null
                  }
                  Update: {
                    "activation_pin_hash"?: string | null,"code"?: string,"colour"?: string | null,"created_at"?: string,"finish"?: string | null,"is_free"?: boolean,"label"?: string | null,"lost_at"?: string | null,"product"?: Database["public"]['Enums']["product"],"retired_at"?: string | null,"size"?: string | null,"state"?: Database["public"]['Enums']["tag_state"],"test_until"?: string | null,"type"?: Database["public"]['Enums']["tag_type"] | null
                  }
                  Relationships: [
                    
                  ]
                }
          }
          Views: {
            [_ in never]: never
          }
          Functions: {
            "check_rate_limit":
{ Args: { "p_key": string,"p_max": number,"p_window_seconds": number }; Returns: boolean
                           },
"finder_reply":
{ Args: { "p_body": string,"p_token_hash": string }; Returns: undefined
                           },
"get_finder_page":
{ Args: { "p_input": string }; Returns: Json
                           },
"get_report_view":
{ Args: { "p_token_hash": string }; Returns: Json
                           },
"mark_found":
{ Args: { "p_code": string }; Returns: Database["public"]['Enums']["tag_state"]
                           },
"mark_lost":
{ Args: { "p_code": string }; Returns: Database["public"]['Enums']["tag_state"]
                           },
"mark_returned":
{ Args: { "p_code": string }; Returns: Database["public"]['Enums']["tag_state"]
                           },
"owner_reply":
{ Args: { "p_body": string,"p_code": string }; Returns: undefined
                           },
"record_scan":
{ Args: { "p_city": string,"p_code": string,"p_ua_class": string }; Returns: undefined
                           },
"retire_tag":
{ Args: { "p_code": string }; Returns: Database["public"]['Enums']["tag_state"]
                           },
"setup_blank_tag":
{ Args: { "p_code": string,"p_finder_message": string,"p_name": string,"p_type": Database["public"]['Enums']["tag_type"] }; Returns: Database["public"]['Enums']["tag_state"]
                           },
"submit_report":
{ Args: { "p_code": string,"p_contact_email": string,"p_lang": string,"p_note": string,"p_place": string,"p_token_hash": string,"p_where": Database["public"]['Enums']["where_now"] }; Returns: string
                           }
          }
          Enums: {
            "member_role": "owner","message_sender": "owner"|"finder"|"system","product": "sticker"|"keychain"|"pet_tag"|"luggage_label"|"lock_screen","return_state": "open"|"handed_over"|"closed","tag_state": "unclaimed"|"unlinked"|"normal"|"lost"|"return_active"|"retired","tag_type": "item"|"travel"|"pet","where_now": "with_me"|"staff"|"safe_place"
          }
          CompositeTypes: {
            [_ in never]: never
          }
        }
}

type DatabaseWithoutInternals = Omit<Database, '__InternalSupabase'>

type DefaultSchema = DatabaseWithoutInternals[Extract<keyof Database, "public">]

export type Tables<
  DefaultSchemaTableNameOrOptions extends
    | keyof (DefaultSchema["Tables"] & DefaultSchema["Views"])
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof (DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"] &
        DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Views"])
    : never = never
> = DefaultSchemaTableNameOrOptions extends { schema: keyof DatabaseWithoutInternals }
  ? (DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"] &
      DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Views"])[TableName] extends {
      Row: infer R
    }
    ? R
    : never
  : DefaultSchemaTableNameOrOptions extends keyof (DefaultSchema["Tables"] & DefaultSchema["Views"])
  ? (DefaultSchema["Tables"] & DefaultSchema["Views"])[DefaultSchemaTableNameOrOptions] extends {
      Row: infer R
    }
    ? R
    : never
  : never

export type TablesInsert<
  DefaultSchemaTableNameOrOptions extends
    | keyof DefaultSchema["Tables"]
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"]
    : never = never
> = DefaultSchemaTableNameOrOptions extends { schema: keyof DatabaseWithoutInternals }
  ? DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Insert: infer I
    }
    ? I
    : never
  : DefaultSchemaTableNameOrOptions extends keyof DefaultSchema["Tables"]
  ? DefaultSchema["Tables"][DefaultSchemaTableNameOrOptions] extends {
      Insert: infer I
    }
    ? I
    : never
  : never

export type TablesUpdate<
  DefaultSchemaTableNameOrOptions extends
    | keyof DefaultSchema["Tables"]
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"]
    : never = never
> = DefaultSchemaTableNameOrOptions extends { schema: keyof DatabaseWithoutInternals }
  ? DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Update: infer U
    }
    ? U
    : never
  : DefaultSchemaTableNameOrOptions extends keyof DefaultSchema["Tables"]
  ? DefaultSchema["Tables"][DefaultSchemaTableNameOrOptions] extends {
      Update: infer U
    }
    ? U
    : never
  : never

export type Enums<
  DefaultSchemaEnumNameOrOptions extends
    | keyof DefaultSchema["Enums"]
    | { schema: keyof DatabaseWithoutInternals },
  EnumName extends DefaultSchemaEnumNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaEnumNameOrOptions["schema"]]["Enums"]
    : never = never
> = DefaultSchemaEnumNameOrOptions extends { schema: keyof DatabaseWithoutInternals }
  ? DatabaseWithoutInternals[DefaultSchemaEnumNameOrOptions["schema"]]["Enums"][EnumName]
  : DefaultSchemaEnumNameOrOptions extends keyof DefaultSchema["Enums"]
  ? DefaultSchema["Enums"][DefaultSchemaEnumNameOrOptions]
  : never

export type CompositeTypes<
  PublicCompositeTypeNameOrOptions extends
    | keyof DefaultSchema["CompositeTypes"]
    | { schema: keyof DatabaseWithoutInternals },
  CompositeTypeName extends PublicCompositeTypeNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[PublicCompositeTypeNameOrOptions["schema"]]["CompositeTypes"]
    : never = never
> = PublicCompositeTypeNameOrOptions extends { schema: keyof DatabaseWithoutInternals }
  ? DatabaseWithoutInternals[PublicCompositeTypeNameOrOptions["schema"]]["CompositeTypes"][CompositeTypeName]
  : PublicCompositeTypeNameOrOptions extends keyof DefaultSchema["CompositeTypes"]
  ? DefaultSchema["CompositeTypes"][PublicCompositeTypeNameOrOptions]
  : never

export const Constants = {
  "public": {
          Enums: {
            "member_role": ["owner"],"message_sender": ["owner", "finder", "system"],"product": ["sticker", "keychain", "pet_tag", "luggage_label", "lock_screen"],"return_state": ["open", "handed_over", "closed"],"tag_state": ["unclaimed", "unlinked", "normal", "lost", "return_active", "retired"],"tag_type": ["item", "travel", "pet"],"where_now": ["with_me", "staff", "safe_place"]
          }
        }
} as const
